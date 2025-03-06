import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

parking_file = "data\Cleaned_Annual_Parking_Study_Data_20250220.csv"
weather_file = "data\processed_weather_data.csv"


parking_df = pd.read_csv(parking_file, parse_dates=["Date Time"])
weather_df = pd.read_csv(weather_file, parse_dates=["timestamp"])

# Rename columns for consistency
weather_df.rename(columns={"timestamp": "Date Time"}, inplace=True)

# Merge datasets on Date Time & Region
merged_df = pd.merge(parking_df, weather_df, on=["Date Time"], how="inner")

# Save merged dataset
merged_file = "merged_parking_weather_data.csv"
merged_df.to_csv(merged_file, index=False)
print(f"Merged dataset saved at: {merged_file}")