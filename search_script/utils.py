# search_script/utils.py
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)

def log_search_result(result):
    """Log search results."""
    if result:
        logging.info(f"Found result: {result}")
    else:
        logging.info("No result found.")
