import pandas as pd
import os
import re  # Import regex for better sanitization

# Read the main CSV file with location data
df = pd.read_csv("data/WPP2022_PopulationBySingleAgeSex_Medium_1950-2021.csv", low_memory=False)

# Identify the base directory of the project
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, 'data')

# Define the output directory where the grouped CSV files will be saved
output_dir = os.path.join(data_dir, 'loc_type_group')
# Create the directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Select only the required columns
selected_columns = ['LocID', 'Location', 'LocTypeName', 'Time', 'PopMale', 'PopFemale', 'PopTotal', 'AgeGrp']
data = df.loc[:, selected_columns].copy()

# Clean the AgeGrp column
data.loc[:, 'AgeGrp'] = data['AgeGrp'].replace('100+', '100')
data.loc[:, 'AgeGrp'] = data['AgeGrp'].astype(int)

# Group the data by 'LocTypeName' and save each group as a separate CSV file
grouped = data.groupby(['LocTypeName'])

for loc_type, group_data in grouped:
    # If loc_type is a tuple, extract the first element
    if isinstance(loc_type, tuple):
        loc_type = loc_type[0]

    # Properly sanitize the location type name
    # Sanitize the location name by replacing '/' to form valid file names
    sanitized_loc_type = loc_type.replace('/', '_')  # Replace '/' to ensure valid file names

    # Construct the file path for each group using its sanitized LocTypeName
    file_path = os.path.join(output_dir, f'Loc_type_{sanitized_loc_type}.csv')

    # Save each grouped DataFrame to a separate CSV file
    group_data.to_csv(file_path, index=False)
    print(f"Đã xuất file: {file_path}")