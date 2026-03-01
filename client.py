import time
import requests
import logging
from typing import Any, Dict

from auth import Auth
from endpoints.fields import FieldsEndpoint
from endpoints.operations import OperationsEndpoint
from endpoints.crops import CropsEndpoint
from exceptions import (
    CropwiseAPIError, ServerError, PermissionDeniedError, NotFoundError, 
    DeletionNotAllowed, UnprocessableEntityError
)
from utils import setup_logging

setup_logging()
logger = logging.getLogger("cropwise_client")


class CropwiseClient:
    """
    A client for interacting with the Cropwise API.
    Documentation: https://cropwiseoperations.docs.apiary.io/
    """
    def __init__(self, email: str, password: str, base_url: str = None):
        self.base_url = base_url or "https://operations.cropwise.com/api/v3"
        self.auth = Auth(email, password, self.base_url)
        self.token = self.auth.login()
        
        self.fields = FieldsEndpoint(self)
        self.operations = OperationsEndpoint(self)
        self.crops = CropsEndpoint(self)

    def _headers(self, method: str = "GET") -> Dict[str, str]:
        """
        Returns headers for the request, including the authentication token.

        :param method: HTTP method (e.g., 'GET', 'POST').
        :return: A dictionary of request headers.
        """
        headers = {"Content-Type": "application/json"} if method in ["POST", "PUT"] else {}
        headers["X-User-Api-Token"] = self.token
        return headers

    def _request(self, method: str, path: str, retries: int = 3, **kwargs: Any) -> Any:
        """
        Internal method to make requests to the API, with built-in re-authentication.
        
        :param method: HTTP method (e.g., 'GET', 'POST').
        :param path: API endpoint path.
        :param retries: Number of retries for network errors.
        :param kwargs: Additional arguments for requests.request (e.g., json, params).
        :return: The 'data' portion of the JSON response.
        """
        url = self.base_url + path
        for attempt in range(retries + 1):
            try:
                logger.info(f"Executing {method} request to {url} with params {kwargs.get('params')}")
                response = requests.request(
                    method,
                    url,
                    headers=self._headers(method=method),
                    timeout=(5, 30),
                    **kwargs
                )

                if response.status_code == 401:
                    logger.warning("Authentication token is invalid or expired. Re-authenticating.")
                    self.token = self.auth.login()
                    continue  # Retry the request with the new token

                if response.status_code == 302:
                    raise DeletionNotAllowed("Deletion not allowed for this resource.")
                
                if response.status_code == 403:
                    if method == "DELETE":
                        logger.info("Resource successfully deleted.")
                        return True
                    else:
                        raise PermissionDeniedError("Access denied. Check your permissions.")

                if response.status_code == 404:
                    raise NotFoundError("Resource not found.")
                
                if response.status_code == 422:
                    logger.error(f"Unprocessable Entity. Details: {response.text}")
                    raise UnprocessableEntityError("Unprocessable entity.")

                if response.status_code in (500, 502, 503, 504):
                    raise ServerError(f"Server error: {response.status_code}")

                # Handle successful but empty responses
                if response.status_code == 204:
                    return None

                response_json = response.json()
                return response_json.get("data")

            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                logger.warning(f"Network error: {e}. Attempt {attempt + 1} of {retries + 1}.")
                if attempt == retries:
                    raise CropwiseAPIError(f"Networking error after {retries} retries: {e}") from e
                time.sleep(2 ** attempt)  # Exponential backoff
        
        raise CropwiseAPIError(f"Request failed after {retries + 1} attempts.")

