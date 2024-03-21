import requests
import csv
from io import StringIO
from supabase import create_client
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv()

# Access environment variables
db_host = os.getenv("SU")
db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASS")

# Initialize Supabase client
client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Function to download CSV from URL and insert data into Supabase table
def download_and_insert_csv(url):
    # Download CSV from URL
    response = requests.get(url)
    

# Example usage
csv_url = 'URL_OF_YOUR_CSV_FILE'
download_and_insert_csv(csv_url)