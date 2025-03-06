import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned parking and weather datasets
parking_file = "data\Cleaned_Annual_Parking_Study_Data_20250220.csv"
weather_file = "data/processed_weather_data.csv"

parking_df = pd.read_csv(parking_file, parse_dates=["Date Time"])
weather_df = pd.read_csv(weather_file, parse_dates=["timestamp"])

# Rename columns for consistency
weather_df.rename(columns={"timestamp": "Date Time"}, inplace=True)

# Merge datasets on Date Time & Region
merged_df = pd.merge(parking_df, weather_df, on=["Date Time"], how="inner")

# Save merged dataset
merged_file = "data/merged_parking_weather_data.csv"
merged_df.to_csv(merged_file, index=False)
print(f"Merged dataset saved at: {merged_file}")

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(merged_df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap Between Weather & Parking Data")
plt.savefig("merged_visualizations/correlation_heatmap.png")
plt.close()

# Precipitation vs. Parking Demand
plt.figure(figsize=(8, 5))
sns.scatterplot(x=merged_df["precipitation"], y=merged_df["Total_Vehicle_Count"], alpha=0.5, color="blue")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Total Vehicle Count")
plt.title("Impact of Precipitation on Parking Demand")
plt.savefig("merged_visualizations/precipitation_vs_parking.png")
plt.close()

# Temperature vs. Parking Demand
plt.figure(figsize=(8, 5))
sns.scatterplot(x=merged_df["temperature"], y=merged_df["Total_Vehicle_Count"], alpha=0.5, color="red")
plt.xlabel("Temperature (°C)")
plt.ylabel("Total Vehicle Count")
plt.title("Impact of Temperature on Parking Demand")
plt.savefig("merged_visualizations/temperature_vs_parking.png")
plt.close()

# Wind Speed vs. Parking Demand
plt.figure(figsize=(8, 5))
sns.scatterplot(x=merged_df["wind_speed"], y=merged_df["Total_Vehicle_Count"], alpha=0.5, color="green")
plt.xlabel("Wind Speed (m/s)")
plt.ylabel("Total Vehicle Count")
plt.title("Impact of Wind Speed on Parking Demand")
plt.savefig("merged_visualizations/wind_speed_vs_parking.png")
plt.close()

print("All visualizations saved.")
