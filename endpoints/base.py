from abc import ABC, abstractmethod
from typing import List, Dict, Any, TypeVar, Type

T = TypeVar('T')


class BaseEndpoint(ABC):
    """Base class for API endpoints."""
    def __init__(self, client: 'CropwiseClient'):
        self.client = client

    @property
    @abstractmethod
    def endpoint(self) -> str:
        """The endpoint path, e.g., '/fields'."""
        pass


class ReadOnlyEndpoint(BaseEndpoint, ABC):
    """Base class for read-only endpoints."""

    def list(self, **kwargs: Any) -> List[Dict[str, Any]]:
        """Retrieve a list of resources."""
        return self.client._request("GET", self.endpoint, params=kwargs)

    def get(self, resource_id: int) -> Dict[str, Any]:
        """Retrieve a single resource by its ID."""
        return self.client._request("GET", f"{self.endpoint}/{resource_id}")

    def get_ids(self) -> List[int]:
        """Retrieve a list of all resource IDs."""
        return self.client._request("GET", f"{self.endpoint}/ids")

    def get_count(self) -> int:
        """Get the total number of resources."""
        response = self.client._request("GET", f"{self.endpoint}/count")
        return response.get('count', 0) if isinstance(response, dict) else 0

    def get_changes(self, from_time: str, to_time: str, **kwargs: Any) -> List[Dict[str, Any]]:
        """Retrieve a list of changes within a time range."""
        params = {'from_time': from_time, 'to_time': to_time}
        params.update(kwargs)
        return self.client._request("GET", f"{self.endpoint}/changes", params=params)

    def get_changes_ids(self, from_time: str, to_time: str, **kwargs: Any) -> List[Dict[str, Any]]:
        """Retrieve a list of changed resource IDs within a time range."""
        params = {'from_time': from_time, 'to_time': to_time}
        params.update(kwargs)
        return self.client._request("GET", f"{self.endpoint}/changes_ids", params=params)

    def mass_request(self, ids: List[int]) -> List[Dict[str, Any]]:
        """Request a large number of resources by their IDs."""
        payload = {"data": ids}
        return self.client._request("POST", f"{self.endpoint}/mass_request", json=payload)


class WritableEndpoint(ReadOnlyEndpoint, ABC):
    """Base class for endpoints that support create, update, and delete operations."""

    def create(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new resource."""
        payload = {"data": data}
        return self.client._request("POST", self.endpoint, json=payload)

    def update(self, resource_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing resource."""
        payload = {"data": data}
        return self.client._request("PUT", f"{self.endpoint}/{resource_id}", json=payload)

    def delete(self, resource_id: int) -> bool:
        """Delete a resource by its ID."""
        return self.client._request("DELETE", f"{self.endpoint}/{resource_id}")
