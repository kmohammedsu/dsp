import os

# Define the folder structure
folders = [
    "data",
    "notebooks",
    "scripts",
    "reports",
    "models",
    "logs"
]

# Define files with their paths
files = {
    "data/Annual_Parking_Study_Data_20250220.csv": "",
    "data/cleaned_parking_data.csv": "",
    "data/weather_data.json": "",
    "notebooks/01_data_cleaning.ipynb": "",
    "notebooks/02_exploratory_analysis.ipynb": "",
    "notebooks/03_model_building.ipynb": "",
    "scripts/data_cleaning.py": "# Data cleaning script",
    "scripts/eda_visualization.py": "# EDA visualization script",
    "scripts/weather_fetch.py": "# Script to fetch weather data",
    "scripts/main.py": "# Main execution script",
    "reports/eda_summary.pdf": "",
    "reports/final_presentation.pptx": "",
    "models/parking_demand_model.pkl": "",
    "logs/data_processing.log": "",
    "requirements.txt": "pandas\nmatplotlib\nseaborn\nscikit-learn\n",
    "README.md": "# Parking Analysis Project\n\nThis project analyzes parking trends in Seattle.\n"
}

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create files
for file_path, content in files.items():
    with open(file_path, "w") as f:
        f.write(content)

print("✅ Project structure created successfully!")
