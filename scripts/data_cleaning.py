import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# File Path
file_path = r"data/Annual_Parking_Study_Data_20250220.csv"
output_file_path = os.path.join(os.path.dirname(file_path), "Cleaned_" + os.path.basename(file_path))

# Load Data
parking_df = pd.read_csv(file_path, dtype=str, low_memory=False)

# Step 1: Data Cleaning by Convert Numeric Columns (Handle Errors)
numeric_cols = ["Parking_Spaces", "Total_Vehicle_Count", "Dp_Count", "Rpz_Count"]
for col in numeric_cols:
    parking_df[col] = pd.to_numeric(parking_df[col], errors="coerce")

# Convert DateTime Columns Properly (Fix: Handle Different Date Formats)
date_cols = ["Date Time", "Time Stamp"]
for col in date_cols:
    if col in parking_df.columns:
        parking_df[col] = pd.to_datetime(parking_df[col], errors="coerce", format="%m/%d/%Y %H:%M")

# Convert Categorical Columns (Fix: Replace NaN with 'Unknown' only if category exists)
categorical_cols = ["Study_Area", "Sub_Area"]
for col in categorical_cols:
    if col in parking_df.columns:
        parking_df[col] = parking_df[col].astype("category")
        parking_df[col] = parking_df[col].cat.add_categories(["Unknown"])
        parking_df[col].fillna("Unknown", inplace=True)

# Drop rows where DateTime is missing **before** numeric filtering
parking_df.dropna(subset=["Date Time"], inplace=True)

# Fill Missing Numeric Values with Median **before filtering negative values**
parking_df[numeric_cols] = parking_df[numeric_cols].fillna(parking_df[numeric_cols].median())

# Ensure Total_Vehicle_Count NaNs are filled with 0 before filtering
parking_df.loc[:, "Total_Vehicle_Count"] = parking_df["Total_Vehicle_Count"].fillna(0)

# Drop rows where all numeric values are missing
to_drop = parking_df[numeric_cols].isna().all(axis=1)
parking_df = parking_df[~to_drop]

# Remove Negative Values in Total_Vehicle_Count
parking_df = parking_df[parking_df["Total_Vehicle_Count"] >= 0]

# Set DateTime column as index for time-series analysis
parking_df.set_index("Date Time", inplace=True)

# Save Cleaned Data to CSV in the Same Folder
parking_df.to_csv(output_file_path)

print(f"Cleaned data saved to: {output_file_path}")
