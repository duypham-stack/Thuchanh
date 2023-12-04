import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Đọc dữ liệu từ file CSV
data = pd.read_csv('Student_Performance.csv')

# Chia dữ liệu thành hai phần: huấn luyện (80%) và kiểm tra (20%)
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Chuẩn bị dữ liệu cho mô hình hồi quy tuyến tính
X_train = train_data[['feature1', 'feature2', ...]].values
y_train = train_data['target_column'].values

X_test = test_data[['feature1', 'feature2', ...]].values
y_test = test_data['target_column'].values

# Thêm cột 1 vào ma trận đầu vào để thực hiện hồi quy tuyến tính
X_train = np.c_[np.ones(X_train.shape[0]), X_train]
X_test = np.c_[np.ones(X_test.shape[0]), X_test]

# Tính toán trọng số của mô hình
weights = np.linalg.inv(X_train.T @ X_train) @ X_train.T @ y_train

# Dự đoán trên dữ liệu kiểm tra
y_pred = X_test @ weights

# Đánh giá hiệu suất của mô hình
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared:", r2)
