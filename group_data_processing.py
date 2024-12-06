import pandas as pd
import os

# Read the main CSV file with location data
df = pd.read_csv("data/WPP2022_PopulationBySingleAgeSex_Medium_1950-2021.csv", low_memory=False)

# Filter the DataFrame to keep only rows where LocTypeName is "Country/Area"
df_filtered = df[df['LocTypeName'] == "Country/Area"]

# Identify the base directory of the project
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')
output_dir = os.path.join(data_dir, 'country_area')

# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Group the filtered data by LocID and save each group as a separate CSV file
grouped = df_filtered.groupby(['LocID', 'Location'])

for (loc_id, location), group_data in grouped:
    sanitized_location = location.replace('/', ' ')  # Replace '/' to ensure valid file names
    file_path = os.path.join(output_dir, f'group_{loc_id}_{sanitized_location}.csv')
    group_data.to_csv(file_path, index=False)
    print(f"Đã xuất file: {file_path}")