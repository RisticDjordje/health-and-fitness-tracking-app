-- retrieves the daily aggregates for a user over the past 7 days. 
-- This includes the total water intake, total calories consumed, total calories burned, and net calories for each day.
-- This can be used to graph the use for each day

SELECT
    Date,
    WaterIntake,
    TotalCaloriesConsumed,
    TotalCaloriesBurned,
    NetCalories
FROM
    DailyActivity
WHERE
    UserID = 1
    AND Date >= Date ('now', '-7 days')
ORDER BY
    Date;