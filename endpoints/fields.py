from typing import List, Optional
from endpoints.base import WritableEndpoint
from models import Field, ChangeRecord


class FieldsEndpoint(WritableEndpoint):
    """
    Endpoint for interacting with Fields in the Cropwise API.
    """
    endpoint = "/fields"

    def list(self, limit: int = 1000, from_id: int = 0) -> List[Field]:
        """
        Retrieves a list of user fields.
        
        :param limit: Maximum number of fields to retrieve.
        :param from_id: Starting ID for pagination.
        :return: A list of Field objects.
        """
        response_data = super().list(limit=limit, from_id=from_id)
        return [Field.from_api(item) for item in response_data]

    def get(self, field_id: int) -> Field:
        """
        Retrieves information about a specific field by its ID.

        :param field_id: The ID of the field.
        :return: A Field object.
        """
        response_data = super().get(field_id)
        return Field.from_api(response_data)

    def get_ids(self) -> List[int]:
        """
        Retrieves a list of all user field IDs.
        
        :return: A list of integers representing field IDs.
        """
        return super().get_ids()

    def count(self) -> int:
        """
        Retrieves the total number of user fields.

        :return: The total number of fields.
        """
        return super().get_count()

    def create(self, field_data: Field) -> Field:
        """
        Creates a new field with the provided data.

        :param field_data: A Field object containing the data for the new field.
        :return: The created Field object.
        """
        response_data = super().create(field_data.to_api())
        return Field.from_api(response_data)

    def update(self, field_id: int, field_data: Field) -> Field:
        """
        Updates information for an existing field.

        :param field_id: The ID of the field to update.
        :param field_data: A Field object with the updated data.
        :return: The updated Field object.
        """
        response_data = super().update(field_id, field_data.to_api())
        return Field.from_api(response_data)

    def delete(self, field_id: int) -> bool:
        """
        Deletes a field by its ID.

        :param field_id: The ID of the field to delete.
        :return: True if deletion was successful.
        """
        return super().delete(field_id)

    def get_changes(self, from_time: str, to_time: str) -> List[Field]:
        """
        Retrieves a list of field changes within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of Field objects that have changed.
        """
        response_data = super().get_changes(from_time=from_time, to_time=to_time)
        return [Field.from_api(item) for item in response_data]

    def get_changes_ids(self, from_time: str, to_time: str) -> List[ChangeRecord]:
        """
        Retrieves a list of IDs of changed fields within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of ChangeRecord objects.
        """
        response_data = super().get_changes_ids(from_time=from_time, to_time=to_time)
        return [ChangeRecord.from_api(item) for item in response_data]

    def mass_request(self, ids: List[int]) -> List[Field]:
        """
        Requests a large number of fields by their IDs.
        
        :param ids: A list of field IDs.
        :return: A list of Field objects.
        """
        response_data = super().mass_request(ids)
        return [Field.from_api(item) for item in response_data]