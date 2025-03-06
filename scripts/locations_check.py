import pandas as pd

# Load the dataset
file_path = "data/Cleaned_Annual_Parking_Study_Data_20250220.csv"  # Update the path if needed
parking_df = pd.read_csv(file_path, dtype=str, low_memory=False)

# Display unique values in the 'Unitdesc' column
unique_unitdesc_values = parking_df["Unitdesc"].unique()

# Print the first 50 unique values
print(unique_unitdesc_values[:50])
