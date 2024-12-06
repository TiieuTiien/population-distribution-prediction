import os
import pandas as pd

# Specify the directory path
directory_path = 'data/group/'

# List all files in the directory
files = [name for name in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, name))]

# Iterate over each file and count the rows
for file_name in files:
    file_path = os.path.join(directory_path, file_name)
    # Read the file using Pandas
    df = pd.read_csv(file_path)
    # Count the number of rows
    row_count = len(df)
    print(f'File: {file_name} - Number of rows: {row_count}')