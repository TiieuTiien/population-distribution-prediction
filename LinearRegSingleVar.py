import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

#đọc dữ liệu
df = pd.read_csv("data/cleaned/group_4_Afghanistan_cleaned.csv", low_memory=False)

dotuoi_input = float(input("Nhap do tuoi muon du bao:"))
# Dữ liệu mẫu (độ ẩm và nhiệt độ)
X = df['AgeGrp']  # Độ ẩm (%)
Y = df['PopTotal']  # Nhiệt độ (°C)
X = np.array(X).reshape(-1, 1)  # Reshape để phù hợp với scikit-learn

print(Y.shape)
print(X.shape)
print(X)
print(Y)
#Trong bài này, chúng ta chưa cần chia tệp dữ liệu

# Tạo và huấn luyện mô hình hồi quy tuyến tính
model = LinearRegression()
model.fit(X, Y)

# Dự đoán nhiệt độ dựa trên độ ẩm
new_humidity = np.array([[dotuoi_input]])  # Độ ẩm mới để dự đoán nhiệt độ
predicted_population = model.predict(new_humidity)

print(f"Dự đoán dan so cho độ tuoi {dotuoi_input} là:", predicted_population[0], " nghin nguoi")