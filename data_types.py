import pandas as pd

df = pd.read_csv("data/country_area/group_4_Afghanistan.csv", low_memory=False)

# Create a dictionary to store the column names by data type
data_types = {}

# Iterate over each column and classify them by their data type
for column, dtype in df.dtypes.items():
    dtype_str = str(dtype)  # Convert dtype to string for usage as a key
    if dtype_str not in data_types:
        data_types[dtype_str] = []  # Initialize a list for the new data type
    data_types[dtype_str].append(column)

# Convert the lists of column names to comma-separated strings
for dtype in data_types:
    data_types[dtype] = ', '.join(data_types[dtype])

# Print the resulting dictionary
# print(data_types)

import numpy as np

# Convert the data_types dictionary into a NumPy array
numpy_table = np.array(list(data_types.items()), dtype=object)

# Print the resulting NumPy array

# Loop through the array
for row in numpy_table:
    print('|', end='')
    for element in row:
        print(element, '|', end='')
    print()

print(df.dtypes)