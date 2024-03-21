import requests
from zipfile import ZipFile
import io
import datetime
import os
import shutil

def get_data():
    # URL of the ZIP file containing the CSV
    url = 'https://openpowerlifting.gitlab.io/opl-csv/files/openpowerlifting-latest.zip'

    # Send a GET request to the URL to download the ZIP file
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Read the content of the response as bytes
        zip_data = io.BytesIO(response.content)
        
        # Create a ZipFile object
        with ZipFile(zip_data, "r") as zip_file:
            print(zip_file.namelist)
            for file in zip_file.namelist():
                if file.endswith('.csv'):
                    print(file)
                    zip_file.extract(file, "./raw_data")  
                    print("CSV file extracted and saved successfully.")
                    
                    # Path to the data directory
                    data_dir = "raw_data"

                     # List all files in the data directory
                    files = os.listdir(data_dir + "/" + str(file)[: -41])
                
                    os.rename("raw_data/" + str(file), "raw_data/raw_data.csv")
                    # Specify the path of the folder to be removed
                    folder_path = data_dir + "/" + str(file)[: -41]
                    # Remove the folder
                    shutil.rmtree(folder_path)
        # If the request was not successful, print an error message
        print("Failed to download ZIP file")
        
def main():
    # Every day get an updated raw dataset
    current_date = datetime.datetime.now().strftime("%x")
    first_time = True
    while True:
        new_date = datetime.datetime.now().strftime("%x")
        if new_date > current_date or first_time:
            first_time = False
            current_date = new_date
            get_data()
    
        
if __name__ == "__main__":
    main()