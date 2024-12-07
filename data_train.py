import pandas as pd

# Load the dataset
df_train = pd.read_csv('data/WPP2022_PopulationBySingleAgeSex_Medium_1950-2021.csv', low_memory=False)

df_train.drop('SDMX_code', axis=1, inplace=True)

# Select only numeric types
df_train_numeric = df_train.select_dtypes(include='number')
df_train_cleaned = df_train_numeric.dropna()

# Calculate the desired statistics
statistics = {
    "min": df_train_cleaned.min(),
    "mean": df_train_cleaned.mean(),
    "std": df_train_cleaned.std(),
    "max": df_train_cleaned.max()
}

# Get quantiles
quantiles = df_train_cleaned.apply(lambda x: x.quantile([0.25, 0.5, 0.75]))
quantiles.index = ['0.25', '0.50', '0.75']  # Set readable index for quantiles

# Combine all into a single DataFrame for consistency with quantiles format.
summary_stats = pd.DataFrame(statistics).T
summary_stats.index = ["min", "mean", "std", "max"]

# Combine quantiles and other statistics for final output
combined_stats = pd.concat([quantiles, summary_stats])

# Print the combined statistics
print("Statistics (min, max, mean, std, and quantiles):")
print(combined_stats.to_string())

# Check for non-matching rows between MidPeriod and Time
non_matching_train = df_train[df_train['MidPeriod'] != df_train['Time']]
# Count the number of non-matching rows
non_matching_count_train = non_matching_train.shape[0]
print(f"Number of non-matching rows train between 'MidPeriod' and 'Time': {non_matching_count_train}")
print(f'Number of rows in the CSV file: {len(df_train):,}')

# Check for non-matching rows between MidPeriod and Time
non_matching_cleaned = df_train_cleaned[df_train_cleaned['MidPeriod'] != df_train_cleaned['Time']]
# Count the number of non-matching rows
non_matching_count_cleaned = non_matching_cleaned.shape[0]
print(f"Number of non-matching rows cleaned between 'MidPeriod' and 'Time': {non_matching_count_cleaned}")
print(f'Number of rows in the CSV file: {len(df_train_cleaned):,}')

# Identify columns with any missing values
columns_with_na = df_train_numeric.columns[df_train_numeric.isna().any()]
# Print the columns with NA value
print("Dropped columns due to missing values:")
for column in columns_with_na:
    print(column)

# # Select only numeric types
# df_train_numeric = df_train.select_dtypes(include='number')
#
# # Identify rows with any missing values
# rows_with_na = df_train_numeric[df_train_numeric.isna().any(axis=1)]
#
# # Drop rows with missing values
# df_train_cleaned = df_train_numeric.dropna()
#
# # Print the data of the removed rows
# print("Data of removed rows due to missing values:")
# print(rows_with_na.to_string(index=False))