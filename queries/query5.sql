-- Calculate and return the averages for a user over the past 7 days. 
-- This includes the total water intake, total calories consumed, total calories burned, and net calories for each day.
-- This can be used to graph the use for each day

SELECT
    AVG(WaterIntake) AS AvgWaterIntake,
    AVG(TotalCaloriesConsumed) AS AvgTotalCaloriesConsumed,
    AVG(TotalCaloriesBurned) AS AvgTotalCaloriesBurned,
    AVG(NetCalories) AS AvgNetCalories
FROM
    DailyActivity
WHERE
    UserID = 1
    AND Date >= Date ('now', '-7 days');