# Import required libraries
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd
import os

# Step 1: Load the dataset
# Load your data with `low_memory=False` to handle large datasets efficiently
df = pd.read_csv("data/loc_type_group/Loc_type_Country_Area.csv", low_memory=False)

# Early-Stage Exploration and Comments About Data
# Assume the dataset has columns: 'Time', 'AgeGrp', 'Location', and 'PopTotal'.
# 'Time' and 'AgeGrp' are numerical features, 'Location' is categorical, and 'PopTotal' is the target.

# Step 2: Select features including the categorical column 'Location'
selected_columns = ['Time', 'AgeGrp', 'Location']  # Features including categorical variable
target_column = 'PopTotal'  # Target

X = df[selected_columns]  # Feature set (now includes Location)
Y = df[target_column]  # Target variable

# Step 3: Apply Target Encoding for the categorical variable ('Location')

# Calculate the mean of the target ('PopTotal') for each Location
location_mean_target = X.join(Y).groupby('Location')['PopTotal'].mean()

# Map the Location column to its corresponding mean target value
X['Location_encoded'] = X['Location'].map(location_mean_target)

# Drop the original 'Location' column as it has been encoded
X = X.drop('Location', axis=1)

# Step 4: Scale the numerical features using StandardScaler
# The 'Time' and 'AgeGrp' columns need scaling (Z-score normalization)

# Initialize the scaler and fit-transform only the numerical columns
scaler = StandardScaler()
X_scaled_numeric = scaler.fit_transform(X[['Time', 'AgeGrp']])  # Scale only numerical columns

# Save scaler attributes for potential use in predictions
scaler_attributes = {
    column: {
        "mean": scaler.mean_[i],
        "std": scaler.scale_[i],
    }
    for i, column in enumerate(['Time', 'AgeGrp'])
}

# Combine the scaled numeric features with the encoded 'Location' feature
# Concatenate the scaled numeric values and encoded categorical values into a single feature set
X_scaled = pd.DataFrame(X_scaled_numeric, columns=['Scaled_Time', 'Scaled_AgeGrp'])
X_scaled['Location_encoded'] = X['Location_encoded'].values

# Convert X_scaled to a NumPy array for use in machine learning
X_scaled = X_scaled.to_numpy()

# Step 5: Split the scaled data into training and testing sets
train_X, test_X, train_Y, test_Y = train_test_split(X_scaled, Y, test_size=0.1, random_state=42)

# Step 6: Perform multivariate regression using LinearRegression
# Initialize and train Linear Regression
model = LinearRegression()
model.fit(train_X, train_Y)  # Train the model on the training data
model.save("")

# Step 7: Predict on the test set and evaluate the model's performance
y_pred = model.predict(test_X)

# Evaluate the model using performance metrics
mae = mean_absolute_error(test_Y, y_pred)  # Mean Absolute Error
mse = mean_squared_error(test_Y, y_pred)  # Mean Squared Error
r2 = r2_score(test_Y, y_pred)  # R-squared value

# Output the evaluation results
print("Model Evaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R-Squared Value (R2):", r2)

# Step 8: Use the model for prediction on new data
# Define new data including a 'Location' feature
time_to_predict = 1986
age_group_to_predict = 30
location_to_predict = 'SampleLocation'

# Encode the Location feature using the target-encoded mapping
# If the location does not exist in the training data, use a fallback (e.g., the global mean of PopTotal)
location_encoded = location_mean_target.get(location_to_predict, Y.mean())  # Fallback to global mean

# Standardize the prediction input for 'Time' and 'AgeGrp' using saved scaler attributes
normalized_time = (time_to_predict - scaler_attributes['Time']['mean']) / scaler_attributes['Time']['std']
normalized_age_grp = (age_group_to_predict - scaler_attributes['AgeGrp']['mean']) / scaler_attributes['AgeGrp']['std']

# Combine the scaled numeric values and encoded location for prediction
new_data_scaled = [[normalized_time, normalized_age_grp, location_encoded]]

# Make the prediction
predicted_population = model.predict(new_data_scaled)

# Step 9: Save the prediction result to a file
# Create the prediction message
prediction_message = (
    f"Predicted population for the year {time_to_predict}, age group {age_group_to_predict}, "
    f"and location {location_to_predict} is: {predicted_population[0]:.2f} thousand people\n"
)

# Print the prediction message to the console
print(prediction_message)

# Define the directory and file path for saving the result
directory = "data/result"
file_path = os.path.join(directory, "prediction_result_with_location.txt")

# Check if the directory exists; if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the prediction message to the file
with open(file_path, "w") as file:
    file.write(prediction_message)

print(f"Prediction result saved successfully to {file_path}")