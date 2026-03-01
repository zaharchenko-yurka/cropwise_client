from typing import List
from endpoints.base import WritableEndpoint
from models import Crop, ChangeRecord


class CropsEndpoint(WritableEndpoint):
    """
    Endpoint for interacting with Crops in the Cropwise API.
    """
    endpoint = "/crops"

    def list(self, limit: int = 1000, from_id: int = 0) -> List[Crop]:
        """
        Retrieves a list of crops.

        :param limit: Maximum number of crops to retrieve.
        :param from_id: Starting ID for pagination.
        :return: A list of Crop objects.
        """
        response_data = super().list(limit=limit, from_id=from_id)
        return [Crop.from_api(item) for item in response_data]

    def get(self, crop_id: int) -> Crop:
        """
        Retrieves information about a specific crop by its ID.

        :param crop_id: The ID of the crop.
        :return: A Crop object.
        """
        response_data = super().get(crop_id)
        return Crop.from_api(response_data)

    def create(self, model: Crop) -> Crop:
        """
        Creates a new crop.

        :param model: The Crop object to create.
        :return: The created Crop object.
        """
        response_data = super().create(model.to_api())
        return Crop.from_api(response_data)

    def update(self, crop_id: int, model: Crop) -> Crop:
        """
        Updates an existing crop.

        :param crop_id: The ID of the crop to update.
        :param model: The Crop object with updated data.
        :return: The updated Crop object.
        """
        response_data = super().update(crop_id, model.to_api())
        return Crop.from_api(response_data)

    def delete(self, crop_id: int) -> None:
        """
        Deletes a crop.

        :param crop_id: The ID of the crop to delete.
        """
        super().delete(crop_id)

    def get_changes(self, from_time: str, to_time: str) -> List[Crop]:
        """
        Retrieves a list of crop changes within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of Crop objects that have changed.
        """
        response_data = super().get_changes(from_time=from_time, to_time=to_time)
        return [Crop.from_api(item) for item in response_data]

    def get_changes_ids(self, from_time: str, to_time: str) -> List[ChangeRecord]:
        """
        Retrieves a list of IDs of changed crops within a specific time range.

        :param from_time: Start time in ISO 8601 format.
        :param to_time: End time in ISO 8601 format.
        :return: A list of ChangeRecord objects.
        """
        response_data = super().get_changes_ids(from_time=from_time, to_time=to_time)
        return [ChangeRecord.from_api(item) for item in response_data]

    def mass_request(self, ids: List[int]) -> List[Crop]:
        """
        Requests a large number of crops by their IDs.
        
        :param ids: A list of crop IDs.
        :return: A list of Crop objects.
        """
        response_data = super().mass_request(ids)
        return [Crop.from_api(item) for item in response_data]
