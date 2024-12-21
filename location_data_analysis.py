import pandas as pd

# Read the main CSV file with location data
df = pd.read_csv("data/loc_type_group/Loc_type_Country_Area.csv", low_memory=False)

# Group the filtered data by 'Location'
grouped = df.groupby('Location')

# Print the location names
print("Unique Location Names:")
for location, group_data in grouped:
    print(location)