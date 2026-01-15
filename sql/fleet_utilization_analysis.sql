-- Hertz Fleet Utilization Analysis
-- Public Dataset

-- 1. Fleet demand by fuel type
SELECT
    fuel_type,
    SUM(renter_trips_taken) AS total_trips
FROM fleet_rental_data
GROUP BY fuel_type
ORDER BY total_trips DESC;

-- 2. Average customer rating by fuel type
SELECT
    fuel_type,
    ROUND(AVG(rating), 2) AS avg_rating
FROM fleet_rental_data
GROUP BY fuel_type
ORDER BY avg_rating DESC;

-- 3. Average daily rate by vehicle type
SELECT
    vehicle_type,
    ROUND(AVG(rate_daily), 2) AS avg_daily_rate
FROM fleet_rental_data
GROUP BY vehicle_type
ORDER BY avg_daily_rate DESC;
