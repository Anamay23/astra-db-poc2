# Handles environment loading and Astra DB connection

import os
from dotenv import load_dotenv
from astrapy import DataAPIClient, Database

def connect_to_database() -> Database:
    
    load_dotenv()
    
    endpoint = os.environ.get("API_ENDPOINT")  
    token = os.environ.get("APPLICATION_TOKEN")

    #print("Before checking endpoint and token")

    if not token or not endpoint:
        raise RuntimeError(
            "Environment variables API_ENDPOINT and APPLICATION_TOKEN must be defined"
        )

    # Create an instance of the `DataAPIClient` class
    client = DataAPIClient()

    #print("After creating DataAPIClient")

    database = client.get_database(endpoint, token=token)
    print(f"Connected to database {database.info().name}")

    return database

if __name__ == "__main__":
    connect_to_database()