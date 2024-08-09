from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score, explained_variance_score, median_absolute_error
import numpy as np
import math

# Data for actual and predicted values
y_test = [3.0, -0.5, 2.0, 7.0]
y_pred = [2.5, 0.0, 2.1, 7.8]

# Calculate metrics using scikit-learn functions
mae = mean_absolute_error(y_test, y_pred)  # Mean Absolute Error
mse = mean_squared_error(y_test, y_pred)  # Mean Squared Error
rmse = mean_squared_error(y_test, y_pred, squared=False)  # Root Mean Squared Error (RMSE)
r2 = r2_score(y_test, y_pred)  # R-squared (Coefficient of Determination)
evs = explained_variance_score(y_test, y_pred)  # Explained Variance Score
medae = median_absolute_error(y_test, y_pred)  # Median Absolute Error

print(f"MAE (scikit-learn): {mae:.2f}")
print(f"MSE (scikit-learn): {mse:.2f}")
print(f"RMSE (scikit-learn): {rmse:.2f}")
print(f"R^2 (scikit-learn): {r2:.2f}")
print(f"Explained Variance Score (scikit-learn): {evs:.2f}")
print(f"Median AE (scikit-learn): {medae:.2f}")

# Manual implementations of metrics

# Mean Absolute Error
def mean_absolute_error_manual(y_true, y_pred):
    return sum(abs(y - y_hat) for y, y_hat in zip(y_true, y_pred)) / len(y_true)

# Mean Squared Error
def mean_squared_error_manual(y_true, y_pred):
    return sum((y - y_hat) ** 2 for y, y_hat in zip(y_true, y_pred)) / len(y_true)

# Root Mean Squared Error
def root_mean_squared_error_manual(y_true, y_pred):
    mse = mean_squared_error_manual(y_true, y_pred)
    return math.sqrt(mse)

# R-squared (Coefficient of Determination)
def r2_score_manual(y_true, y_pred):
    mean_y_true = sum(y_true) / len(y_true)  # Mean of actual values
    ss_res = sum((y - y_hat) ** 2 for y, y_hat in zip(y_true, y_pred))  # Residual Sum of Squares
    ss_tot = sum((y - mean_y_true) ** 2 for y in y_true)  # Total Sum of Squares
    return 1 - (ss_res / ss_tot)  # R-squared formula

# Explained Variance Score
def explained_variance_score_manual(y_true, y_pred):
    mean_y_true = sum(y_true) / len(y_true)  # Mean of actual values
    numerator = sum((y - y_hat) ** 2 for y, y_hat in zip(y_true, y_pred))  # Residual Variance
    denominator = sum((y - mean_y_true) ** 2 for y in y_true)  # Total Variance
    return 1 - (numerator / denominator)  # Explained Variance Score formula

# Median Absolute Error
def median_absolute_error_manual(y_true, y_pred):
    return np.median([abs(y - y_hat) for y, y_hat in zip(y_true, y_pred)])  # Median of absolute errors

# Mean Absolute Percentage Error
def mean_absolute_percentage_error_manual(y_true, y_pred):
    return np.mean([abs((y - y_hat) / y) for y, y_hat in zip(y_true, y_pred)]) * 100  # MAPE in percentage

# Adjusted R2
def adjusted_r2_score(y_true, y_pred, n, p):
    r2 = r2_score(y_true, y_pred)
    adjusted_r2 = 1 - ((1 - r2) * (n - 1)) / (n - p - 1)
    return adjusted_r2

# Calculate metrics manually
mae_manual = mean_absolute_error_manual(y_test, y_pred)
mse_manual = mean_squared_error_manual(y_test, y_pred)
rmse_manual = root_mean_squared_error_manual(y_test, y_pred)
r2_manual = r2_score_manual(y_test, y_pred)
evs_manual = explained_variance_score_manual(y_test, y_pred)
medae_manual = median_absolute_error_manual(y_test, y_pred)
mape_manual = mean_absolute_percentage_error_manual(y_test, y_pred)

# Print manual metrics
print(f"MAE (manual): {mae_manual:.2f}")
print(f"MSE (manual): {mse_manual:.2f}")
print(f"RMSE (manual): {rmse_manual:.2f}")
print(f"R^2 (manual): {r2_manual:.2f}")
print(f"Explained Variance Score (manual): {evs_manual:.2f}")
print(f"Median AE (manual): {medae_manual:.2f}")
print(f"MAPE (manual): {mape_manual:.2f}%")
