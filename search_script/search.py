# search_script/search.py
import asyncio
from aiomultiprocess import Pool
from .db_client import get_mongo_client

client = get_mongo_client()

async def list_databases():
    """Retrieve all database names."""
    dbs = await client.list_database_names()
    return dbs

async def search_in_collection(db_name, collection_name, query):
    """Search for fields like email, phone_number, or full_name in a collection."""
    db = client[db_name]
    collection = db[collection_name]
    try:
        result = await collection.find_one(query, {"email": 1, "phone_number": 1, "full_name": 1})
        if result:
            print(f"Found in {db_name}.{collection_name}: {result}")
        return result
    except Exception as e:
        print(f"Error searching in {db_name}.{collection_name}: {e}")
        return None

async def process_database(db_name, query):
    """Process all collections in a single database."""
    db = client[db_name]
    collections = await db.list_collection_names()

    tasks = []
    for collection in collections:
        tasks.append(search_in_collection(db_name, collection, query))

    await asyncio.gather(*tasks)

async def process_databases(dbs, query):
    """Use multiprocessing to process databases in parallel."""
    async with Pool() as pool:
        await pool.map(lambda db: process_database(db, query), dbs)
