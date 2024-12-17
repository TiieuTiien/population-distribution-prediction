from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("data/cleaned/group_4_Afghanistan_cleaned.csv", low_memory=False)

# Step 2: Select features ('Time', 'AgeGrp') and the target ('PopTotal')
selected_columns = ['Time', 'AgeGrp']  # Features
target_column = 'PopTotal'  # Target

X = df[selected_columns]  # Feature set
Y = df[target_column]  # Target variable

# Step 3: Scale the features using StandardScaler (Z-Score normalization)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Optional: Save the attributes (mean, std) for reconversion if needed
scaler_attributes = {
    column: {
        "mean": scaler.mean_[i],
        "std": scaler.scale_[i],
    }
    for i, column in enumerate(selected_columns)
}

# Step 4: Split the scaled data into training and testing sets
train_X, test_X, train_Y, test_Y = train_test_split(X_scaled, Y, test_size=0.1, random_state=42)

# Step 5: Perform multivariate regression using LinearRegression
model = LinearRegression()
model.fit(train_X, train_Y)  # Train the model on the training data

# Step 6: Predict on the test set
y_pred = model.predict(test_X)

# Step 7: Evaluate the model's performance
mae = mean_absolute_error(test_Y, y_pred)  # Mean Absolute Error
mse = mean_squared_error(test_Y, y_pred)  # Mean Squared Error
r2 = r2_score(test_Y, y_pred)  # R-squared value

# Output the results
print("Model Evaluation Metrics:")
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("R-Squared Value (R2):", r2)

import os

# Example Prediction
time_to_predict = 1986
age_group_to_predict = 90

# Standardize the prediction input using the saved scaler attributes
normalized_time = (time_to_predict - scaler_attributes['Time']['mean']) / scaler_attributes['Time']['std']
normalized_age_grp = (age_group_to_predict - scaler_attributes['AgeGrp']['mean']) / scaler_attributes['AgeGrp']['std']

new_data_scaled = [[normalized_time, normalized_age_grp]]
predicted_population = model.predict(new_data_scaled)

# Create a message for the prediction result
prediction_message = (
    f"Predicted population for the year {time_to_predict} and age group {age_group_to_predict} "
    f"is: {predicted_population[0]:.2f} thousand people\n"
)

# Print the message to the console
print(prediction_message)

# Save the result to a file
# Define the directory and file path
directory = "data/result"
file_path = os.path.join(directory, "prediction_result.txt")

# Check if the directory exists; if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the prediction message to the file
with open(file_path, "w") as file:
    file.write(prediction_message)

print(f"Prediction result saved successfully to {file_path}")
