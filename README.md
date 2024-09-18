# mongo_searh_script

How to Run
Clone or set up the project:

bash
Copy code
mkdir mongodb_search_script
cd mongodb_search_script
Install dependencies: Install the required Python libraries using the requirements.txt file.

bash
Copy code
pip install -r requirements.txt
Run the search script: Make the run.sh executable and run it.

bash
Copy code
chmod +x run.sh
./run.sh
This will start the script, which will automatically connect to MongoDB, search across all the databases and collections, and find records that contain the specified fields (email, phone_number, full_name).