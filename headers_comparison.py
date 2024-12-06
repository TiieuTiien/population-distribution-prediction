import os
import pandas as pd

# Define the file path
file_path = 'archive/WPP2022_DeathsBySingleAgeSex_Medium_1950-2021/WPP2022_DeathsBySingleAgeSex_Medium_1950-2021.csv'

# Initialize a list to store headers
headers_list = []

try:
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Extract headers
    headers = df.columns.tolist()
    headers_list.append({'FileName': os.path.basename(file_path), 'Headers': headers})
except Exception as e:
    print(f"Error reading {file_path}: {e}")

# Create a DataFrame to store headers for easy review
headers_df = pd.DataFrame(headers_list)

# Extract filename from path and add to output filename
filename = os.path.basename(file_path).replace('.csv', '')
output_path = f'sample/headers_comparison_{filename}.csv'

# Save the headers to a CSV file for review
headers_df.to_csv(output_path, index=False)

print("Headers extracted and saved to headers_comparison.csv")