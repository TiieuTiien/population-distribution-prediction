import matplotlib.pyplot as plt
import pandas as pd
import os

# Assuming `df` is your DataFrame loaded with the CSV data
# Load your DataFrame here
data = pd.read_csv('data/country_area/group_4_Afghanistan.csv')

# Define the list of columns you want to select
selected_columns = ['LocID', 'Time', 'PopMale', 'PopFemale', 'PopTotal', 'AgeGrp']

# Select the specified columns from the DataFrame
selected_data = data[selected_columns]

df = pd.DataFrame(selected_data)

# Identify numeric columns (or select them manually)
numeric_cols = df.select_dtypes(include='number').columns

# Define the output directory
output_directory = './data/scatter/'

# Create directory if it does not exist
os.makedirs(output_directory, exist_ok=True)

# Generate scatter plots for each pair of numerical columns
for i, x in enumerate(numeric_cols):
    for j, y in enumerate(numeric_cols):
        if i < j:  # To avoid duplicate plots
            plt.figure(figsize=(6, 4))

            # Use median to separate data into two groups for different colors
            median_value = df[x].median()
            group1 = df[df[x] <= median_value]
            group2 = df[df[x] > median_value]

            plt.scatter(group1[x], group1[y], color='blue', label=f'{x} <= median')
            plt.scatter(group2[x], group2[y], color='red', label=f'{x} > median')

            plt.xlabel(x)
            plt.ylabel(y)
            plt.title(f'Scatter Plot: {x} vs {y}')
            plt.legend()

            # Define the file name and save the plot
            file_name = f"scatter_plot_{x}_vs_{y}_2colors.png"
            plt.savefig(os.path.join(output_directory, file_name))

            plt.close()
