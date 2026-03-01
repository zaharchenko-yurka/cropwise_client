from client import CropwiseClient
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("CROPWISE_EMAIL")
password = os.getenv("CROPWISE_PASSWORD")

if __name__ == "__main__":
    if not email or not password:
        print("Please set CROPWISE_EMAIL and CROPWISE_PASSWORD environment variables.")
    else:
        client = CropwiseClient(email=email, password=password)

        # Example 1: Get all field IDs
        try:
            field_ids = client.fields.get_ids()
            print(f"Total fields: {len(field_ids)}")
            if field_ids:
                print(f"First 10 field IDs: {field_ids[:10]}")

                # Example 2: Get details for the first field
                first_field_id = field_ids[0]
                field_details = client.fields.get(first_field_id)
                print(f"\nDetails for field ID {first_field_id}:")
                print(field_details)

        except Exception as e:
            print(f"An error occurred: {e}")

        # Example 3: Get all crops
        try:
            all_crops = client.crops.list()
            print(f"\nTotal crops: {len(all_crops)}")
            if all_crops:
                print(f"First 5 crops: {all_crops[:5]}")
        except Exception as e:
            print(f"An error occurred while fetching crops: {e}")
            
        # Example 4: Get all agro-operations for a specific field
        try:
            if field_ids:
                operations = client.operations.list(field_id=field_ids[0])
                print(f"\nOperations for field ID {field_ids[0]}:")
                print(operations)
        except Exception as e:
            print(f"An error occurred while fetching operations: {e}")