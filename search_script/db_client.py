# search_script/db_client.py
from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI

# Function to return an async MongoDB client
def get_mongo_client():
    client = AsyncIOMotorClient(MONGO_URI)
    return client
