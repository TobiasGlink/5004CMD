import pandas as pd
from scipy.optimize import curve_fit
import numpy as np

df = pd.read_csv('Trips_by_distance.csv')

distance_cols = [col for col in df.columns if "Number of Trips" in col]

long_df = df.melt(value_vars=distance_cols, var_name="Distance Range", value_name="Trip Count")
long_df = long_df.dropna()

distance_mapping = {
    "Number of Trips <1": 0.5,
    "Number of Trips 1-3": 2,
    "Number of Trips 3-5": 4,
    "Number of Trips 5-10": 7.5,
    "Number of Trips 10-25": 17.5,
    "Number of Trips 25-50": 37.5,
    "Number of Trips 50-100": 75,
    "Number of Trips 100-250": 175,
    "Number of Trips 250-500": 375,
    "Number of Trips >=500": 500
}
long_df["Trip Distance (mi)"] = long_df["Distance Range"].map(distance_mapping)

valid_data = long_df.dropna(subset=["Trip Distance (mi)", "Trip Count"])

X = valid_data["Trip Distance (mi)"].values
y = valid_data["Trip Count"].values

X_scaled = X / 1000

y_safe = y + 1e-6  # Add a small constant to all values of y

y_log = np.log(y_safe)

params_log, _ = curve_fit(lambda x, a, b: a * np.exp(-b * x), X_scaled, y_log)

y_pred_log = np.exp(params_log[0] * np.exp(-params_log[1] * X_scaled))

print(f"Log-Exponential Model parameters:\na = {params_log[0]:.4f}\nb = {params_log[1]:.4f}")

print("\nSample Predictions vs Actual:")
for actual, predicted, distance in zip(y[:5], y_pred_log[:5], X[:5]):  # First 5 entries
    print(f"Distance: {distance} mi → Actual: {actual:.2f}, Predicted: {predicted:.2f}")

# Predict for new distance
new_distance = 30  # miles
scaled_distance = new_distance / 1000
predicted_trips = np.exp(params_log[0] * np.exp(-params_log[1] * scaled_distance))
print(f"\nPredicted number of trips at {new_distance} miles: {predicted_trips:.2f}")
