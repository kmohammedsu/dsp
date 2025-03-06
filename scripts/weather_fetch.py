import requests
import json
import os

# Define representative coordinates for key Seattle neighborhoods
seattle_regions = {
    "Downtown Seattle": {"latitude": 47.6062, "longitude": -122.3321},
    "South Lake Union": {"latitude": 47.6235, "longitude": -122.3381},
    "Capitol Hill": {"latitude": 47.6219, "longitude": -122.3194},
    "Ballard": {"latitude": 47.6686, "longitude": -122.3867},
    "Industrial District": {"latitude": 47.5868, "longitude": -122.3331},
}

# API endpoint for historical weather data
base_url = "https://archive-api.open-meteo.com/v1/archive"

# Ensure 'data/' folder exists
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

# Fetch weather data for each neighborhood
weather_data_by_region = {}

for region, coords in seattle_regions.items():
    params = {
        "latitude": coords["latitude"],
        "longitude": coords["longitude"],
        "start_date": "2014-04-08",
        "end_date": "2019-09-19",
        "hourly": ["temperature_2m", "precipitation", "windspeed_10m"],
        "timezone": "America/Los_Angeles",
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data_by_region[region] = response.json()
        print(f"Weather data fetched for {region}")
    else:
        print(f"Failed to fetch data for {region}. Error {response.status_code}: {response.text}")

# Save collected data as JSON
json_file_path = os.path.join(output_folder, "seattle_weather_by_region.json")
with open(json_file_path, "w") as json_file:
    json.dump(weather_data_by_region, json_file, indent=4)

print(f" All weather data saved at: {json_file_path}")
