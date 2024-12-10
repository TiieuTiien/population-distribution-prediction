import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler

# Read the cleaned data
df = pd.read_csv("data/cleaned/group_4_Afghanistan_cleaned.csv", low_memory=False)

# Select only the features 'Time' and 'AgeGrp' and the target variable 'PopTotal'
selected_columns = ['Time', 'AgeGrp']  # Only use Time and AgeGrp as features
target_column = 'PopTotal'  # Target variable

# Prepare input (X) and output (Y)
X = df[selected_columns]
Y = df[[target_column]]  # Ensure Y is a DataFrame for scaling

# Initialize the scalers and apply to the data
scaler_X = StandardScaler()
scaler_Y = StandardScaler()

# Scale the numeric features 'Time' and 'AgeGrp'
X_scaled = scaler_X.fit_transform(X)
Y_scaled = scaler_Y.fit_transform(Y)

# Split data into train and test sets (70% train, 30% test)
train_X, test_X, train_Y, test_Y = train_test_split(X_scaled, Y_scaled, test_size=0.3, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(train_X, train_Y)

# Make predictions on the test set
y_pred = model.predict(test_X)

# Inverse transform predictions to original scale
y_pred_original = scaler_Y.inverse_transform(y_pred)

# Calculate and print regression evaluation metrics (on the original scale)
mae = mean_absolute_error(scaler_Y.inverse_transform(test_Y), y_pred_original)
mse = mean_squared_error(scaler_Y.inverse_transform(test_Y), y_pred_original)
r2 = r2_score(scaler_Y.inverse_transform(test_Y), y_pred_original)

print("Mean Absolute Error on test set (original scale):", mae)
print("Mean Squared Error on test set (original scale):", mse)
print("R-squared on test set (original scale):", r2)

# Predict for a specific time and age group
time_to_predict = 1986  # Example year
age_group_to_predict = 12  # Example age group

# Prepare the new data for prediction
new_data = [[time_to_predict, age_group_to_predict]]  # Only Time and AgeGrp

# Scale the new data using the same scaler
new_data_scaled = scaler_X.transform(new_data)

# Predict using the model
predicted_population_scaled = model.predict(new_data_scaled)

# Inverse transform the prediction to the original scale
predicted_population_original = scaler_Y.inverse_transform(predicted_population_scaled)

# Output the prediction
print(
    f"Dự đoán dân số cho năm {time_to_predict} và độ tuổi {age_group_to_predict} là: {predicted_population_original[0][0]:.2f} nghìn người")