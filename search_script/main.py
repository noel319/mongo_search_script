# search_script/main.py
import asyncio
from .search import list_databases, process_databases

async def main():
    # Define the query to search for fields like email, phone_number, full_name
    query = {
        "$or": [
            {"email": {"$exists": True}},
            {"phone_number": {"$exists": True}},
            {"full_name": {"$exists": True}},
        ]
    }
    
    # List all databases
    dbs = await list_databases()
    print(f"Found {len(dbs)} databases")

    # Process databases in parallel using asyncio and multiprocessing
    await process_databases(dbs, query)

if __name__ == "__main__":
    asyncio.run(main())
