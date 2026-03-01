from typing import List, Optional
from endpoints.base import WritableEndpoint
from models import AgroOperation, ChangeRecord


class OperationsEndpoint(WritableEndpoint):
    """
    Endpoint for interacting with Agro Operations in the Cropwise API.
    """
    endpoint = "/agro_operations"

    def list(
        self,
        limit: int = 1000,
        from_id: int = 0,
        field_id: Optional[int] = None,
        status: Optional[str] = None,
        season: Optional[int] = None,
    ) -> List[AgroOperation]:
        """
        Retrieves a list of agro operations, with optional filtering.

        :param limit: Maximum number of operations to retrieve.
        :param from_id: Starting ID for pagination.
        :param field_id: Filter by a specific field ID.
        :param status: Filter by status (e.g., 'planned', 'in_progress', 'done').
        :param season: Filter by a specific season (year).
        :return: A list of AgroOperation objects.
        """
        params = {"limit": limit, "from_id": from_id}
        if field_id:
            params["field_id"] = field_id
        if status:
            params["status"] = status
        if season:
            params["season"] = season
            
        response_data = super().list(**params)
        return [AgroOperation.from_api(item) for item in response_data]

    def get(self, operation_id: int) -> AgroOperation:
        """
        Retrieves information about a specific agro operation by its ID.

        :param operation_id: The ID of the agro operation.
        :return: An AgroOperation object.
        """
        response_data = super().get(operation_id)
        return AgroOperation.from_api(response_data)

    def get_ids(self) -> List[int]:
        """
        Retrieves a list of all agro operation IDs.

        :return: A list of integers representing agro operation IDs.
        """
        return super().get_ids()

    def count(self) -> int:
        """
        Retrieves the total number of agro operations.

        :return: The total number of agro operations.
        """
        return super().get_count()

    def create(self, operation_data: AgroOperation) -> AgroOperation:
        """
        Creates a new agro operation with the provided data.

        :param operation_data: An AgroOperation object containing the data for the new operation.
        :return: The created AgroOperation object.
        """
        response_data = super().create(operation_data.to_api())
        return AgroOperation.from_api(response_data)

    def update(self, operation_id: int, operation_data: AgroOperation) -> AgroOperation:
        """
        Updates information for an existing agro operation.

        :param operation_id: The ID of the operation to update.
        :param operation_data: An AgroOperation object with the updated data.
        :return: The updated AgroOperation object.
        """
        response_data = super().update(operation_id, operation_data.to_api())
        return AgroOperation.from_api(response_data)

    def delete(self, operation_id: int) -> bool:
        """
        Deletes an agro operation by its ID.

        :param operation_id: The ID of the operation to delete.
        :return: True if deletion was successful.
        """
        return super().delete(operation_id)

    def get_changes(self, from_time: str, to_time: str) -> List[AgroOperation]:
        """
        Retrieves a list of agro operation changes within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of AgroOperation objects that have changed.
        """
        response_data = super().get_changes(from_time=from_time, to_time=to_time)
        return [AgroOperation.from_api(item) for item in response_data]

    def get_changes_ids(self, from_time: str, to_time: str) -> List[ChangeRecord]:
        """
        Retrieves a list of IDs of changed agro operations within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of ChangeRecord objects.
        """
        response_data = super().get_changes_ids(from_time=from_time, to_time=to_time)
        return [ChangeRecord.from_api(item) for item in response_data]

    def mass_request(self, ids: List[int]) -> List[AgroOperation]:
        """
        Requests a large number of agro operations by their IDs.
        
        :param ids: A list of agro operation IDs.
        :return: A list of AgroOperation objects.
        """
        response_data = super().mass_request(ids)
        return [AgroOperation.from_api(item) for item in response_data]