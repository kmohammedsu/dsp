import pandas as pd

# Load the cleaned parking dataset
file_path = "data/Cleaned_Annual_Parking_Study_Data_20250220.csv"  # Adjust the path if necessary
parking_df = pd.read_csv(file_path, parse_dates=["Date Time"])

# Get the min and max dates
start_date = parking_df["Date Time"].min()
end_date = parking_df["Date Time"].max()

print(f"Parking Data Time Frame: {start_date} to {end_date}")