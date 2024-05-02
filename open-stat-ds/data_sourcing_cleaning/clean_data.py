import numpy as np
import pandas as pd
from dotenv import load_dotenv
import os 
import json
from supabase import create_client

def clean_data():
    # Read in raw data
    print("---- Reading Raw Data ----\n")
    df = pd.read_csv('../raw_data/raw_data.csv')
    print("---- Cleaning Data ----\n")
    # Drop unecesssary columns
    columns_to_drop = ['BirthYearClass', 'Squat1Kg', 'Squat2Kg', 'Squat3Kg', 'Squat4Kg', 'Bench1Kg', 'Bench2Kg', 'Bench3Kg', 'Bench4Kg', 'Deadlift1Kg', 'Deadlift2Kg', 'Deadlift3Kg', 'Deadlift4Kg', 'Wilks', 'Glossbrenner', 'Goodlift', 'State', 'MeetCountry', 'MeetState', 'MeetTown', 'MeetName', 'ParentFederation', 'Division']
    df.drop(columns=columns_to_drop, axis=1, inplace=True)
    # Rename columns for ease of use
    df.columns = ['Name', 'Sex', 'Event', 'Equiptment', 'Age', 'Age_Class', 'Bodyweight', 'Weight_Class', 'Squat', 'Bench', 'Deadlift', 'Total', 'Place', 'Dots', 'Tested', 'Country', 'Federation', 'Date']
    # Remove bad data rows
    df_cleaned = df.dropna(subset=['Country', 'Total', 'Age', 'Dots', 'Age_Class', 'Weight_Class'])
    # Fill null values to produce full rows 
    df_cleaned["Tested"] = df_cleaned["Tested"].fillna("No")
    df_cleaned["Squat"] = df_cleaned["Squat"].fillna(0)
    df_cleaned["Bench"] = df_cleaned["Bench"].fillna(0)
    df_cleaned["Deadlift"] = df_cleaned["Deadlift"].fillna(0)
    # Perform Labelling nad encodings for nexessary data 
    mapping = {"Yes": True, "No": False}
    df_cleaned["Tested"] = df_cleaned["Tested"].map(mapping).astype(bool)
    # Ensure each column has correct datatype
    non_numeric_rows = df_cleaned[~df_cleaned['Place'].str.isdigit()]
    numeric_rows = df_cleaned[df_cleaned['Place'].str.isdigit()]
    df_cleaned['Place'] = numeric_rows['Place'].astype(int)
    df_cleaned = df_cleaned.drop(non_numeric_rows.index)
    # Retype where necessary
    df_cleaned['Place'] = df_cleaned['Place'].astype('Int64')
    df_cleaned['Age'] = np.floor(df_cleaned['Age'])
    df_cleaned['Age'] = df_cleaned['Age'].astype('Int64')
    # Now data is nice and clean ready for modelling and the database
    return df_cleaned

def convert_to_insert_array(df):
    insert_array = []
    for _, row in df.iterrows():
        row_dict = {
            "Name": row["Name"],
            "Sex": row["Sex"],
            "Event": row["Event"],
            "Equiptment": row["Equiptment"],
            "Age": row["Age"],
            "Age_Class": row["Age_Class"],
            "Bodyweight": row["Bodyweight"],
            "Weight_Class": row["Weight_Class"],
            "Squat": row["Squat"],
            "Bench": row["Bench"],
            "Deadlift": row["Deadlift"],
            "Total": row["Total"],
            "Place": row["Place"],
            "Dots": row["Dots"],
            "Tested": row["Tested"],
            "Country": row["Country"],
            "Federation": row["Federation"],
            "Date": json.dumps(row["Date"]),
        }
        
        insert_array.append(row_dict)
        
    # Add padding if needed
    leftovers = len(insert_array) % 1000
    if leftovers:
        padd_count = 1000 - leftovers
        padding = [None] * padd_count
        insert_array = insert_array + padding
        
    return insert_array

def save_data(clean_df):
    # First save it to a csv locally for use in the model
    print("---- Saving CSV Locally ----\n")
    clean_df.to_csv('../clean_data/clean_data.csv', index=False)
    # Get the JSON array for PostGresSQL
    print("---- Converting to JSON ----\n")
    data = convert_to_insert_array(clean_df)
    # Load the supabase key and url 
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    master_key = os.getenv("SUPABASE_SECRET_KEY") 
    # Create the supabase client 
    print("---- Connecting to Supabase ----\n")
    client = create_client(url, master_key)
    # Now be tricky and use numpy to create an array of blocks of 100 rows to avoid crashing 
    flights = np.array(data).reshape(-1, 1000).tolist()
    print("---- Uploading Data ----\n")
    for flight in flights:
        _ , _ = client.table('Lifter_Info').insert(flight).execute()
    

if __name__ == "__main__":
    clean_df = clean_data()
    save_data(clean_df)