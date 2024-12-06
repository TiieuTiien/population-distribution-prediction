import pandas as pd

df = pd.read_csv('archive/WPP2022_PopulationBySingleAgeSex_Medium_1950-2021/WPP2022_PopulationBySingleAgeSex_Medium_1950-2021.csv', low_memory=False)

# Print the number of rows
print(f'Number of rows in the CSV file: {len(df):,}')