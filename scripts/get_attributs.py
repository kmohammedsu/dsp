import pandas as pd


file_path = "data\merged_parking_weather_data.csv" 
df = pd.read_csv(file_path, low_memory=False)


attribute_counts = df.count()  
total_values_count = attribute_counts.sum()  


print("Attribute Usage Count:\n")
print(attribute_counts)
print("\nTotal Non-Null Values in Dataset:", total_values_count)


attribute_counts.to_csv("data/attribute_counts.csv", header=["Non-Null Count"])
print("\nAttribute count summary saved as 'data/attribute_counts.csv'")
