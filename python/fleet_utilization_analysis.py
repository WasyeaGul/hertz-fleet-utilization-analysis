import pandas as pd

# -----------------------------
# Load dataset
# -----------------------------
df = pd.read_csv("data/fleet_rental_data.csv")

# Preview data
print("Dataset Preview:")
print(df.head())

# -----------------------------
# Basic data info
# -----------------------------
print("\nDataset Info:")
print(df.info())

# -----------------------------
# Fleet demand by fuel type
# -----------------------------
fleet_demand = (
    df.groupby("fuel_type")["renter_trips_taken"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFleet Demand by Fuel Type:")
print(fleet_demand)

# -----------------------------
# Average customer rating by fuel type
# -----------------------------
avg_rating = (
    df.groupby("fuel_type")["rating"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nAverage Customer Rating by Fuel Type:")
print(avg_rating)

# -----------------------------
# Average daily rate by vehicle type
# -----------------------------
avg_daily_rate = (
    df.groupby("vehicle_type")["rate_daily"]
    .mean()
    .round(2)
    .sort_values(ascending=False)
)

print("\nAverage Daily Rate by Vehicle Type:")
print(avg_daily_rate)

# -----------------------------
# Save summary outputs
# -----------------------------
fleet_demand.to_csv("outputs/fleet_demand_by_fuel_type.csv")
avg_rating.to_csv("outputs/avg_rating_by_fuel_type.csv")
avg_daily_rate.to_csv("outputs/avg_daily_rate_by_vehicle_type.csv")

print("\nAnalysis complete. Output files saved.")
