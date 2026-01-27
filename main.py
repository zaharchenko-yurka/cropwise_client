from client import CropwiseClient
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("CROPWISE_EMAIL")
password = os.getenv("CROPWISE_PASSWORD")

if __name__ == "__main__":
    client = CropwiseClient(email=email, password=password)
    #fields = client.get_fields()
    #print(fields)