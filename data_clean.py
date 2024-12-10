import pandas as pd
import os

# Directory containing the original CSV files
input_dir = "data/country_area/"
# Directory where to save the cleaned CSV files
output_dir = "data/cleaned/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over CSV files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_dir, filename)

        # Load the CSV file
        df = pd.read_csv(file_path, low_memory=False)

        # Select the necessary columns
        selected_columns = ['LocID', 'LocTypeID', 'Time', 'PopMale', 'PopFemale', 'PopTotal', 'AgeGrp']
        df_selected = df[selected_columns]

        # Clean the AgeGrp column
        df_selected.loc[:, 'AgeGrp'] = df_selected['AgeGrp'].replace('100+', '100')
        df_selected.loc[:, 'AgeGrp'] = df_selected['AgeGrp'].astype(int)

        # Generate the cleaned file name
        base_filename = os.path.splitext(filename)[0] + "_cleaned.csv"
        full_path = os.path.join(output_dir, base_filename)

        # Save the cleaned DataFrame
        df_selected.to_csv(full_path, index=False, encoding='utf-8')

        print(f"Processed and saved: {full_path}")