import pandas as pd
from sklearn.decomposition import PCA
import numpy as np


def extract_pca_features(file_path, n_col):
    # Load the dataset from a CSV file
    df = pd.read_csv(file_path, low_memory=False)

    # Select only the required columns
    selected_columns = ['LocID', 'Time', 'PopMale', 'PopFemale', 'PopTotal', 'AgeGrp']
    data = df.loc[:, selected_columns].copy()

    # Convert '100+' in AgeGrp to 100
    data.loc[:, 'AgeGrp'] = data['AgeGrp'].replace('100+', 100).astype(int)

    # Create the PCA model
    model = PCA(n_components=n_col)

    # Fit and transform the data
    pca_result = model.fit_transform(data)

    # Get feature names for the components based on loadings
    components = model.components_
    feature_names = []
    for i in range(n_col):
        # Identify the feature with the highest absolute loading in each principal component
        feature_idx = np.abs(components[i]).argmax()
        feature_names.append(selected_columns[feature_idx])

    # Return the resulting PCA features
    return pca_result, feature_names


# Specify the file path to your CSV file
csv_file_path = 'data/country_area/group_4_Afghanistan.csv'

# Extract PCA features from the specified file
try:
    pca_features, feature_names = extract_pca_features(csv_file_path, 2)
    # Convert PCA results to a DataFrame with descriptive columns
    pca_df = pd.DataFrame(pca_features, columns=feature_names)
    # Save the PCA results to a CSV file
    pca_df.to_csv('pca_results.csv', index=False)
except ValueError as e:
    print(f"Error: {e}")