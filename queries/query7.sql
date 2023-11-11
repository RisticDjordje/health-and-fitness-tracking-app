-- Calculate how much more water the user should drink today to reach their daily goal
WITH UserGoal AS (
    SELECT 
        UserID,
        WaterIntakeGoal
    FROM 
        WaterIntakeGoal
    WHERE 
        UserID = 2
)
SELECT 
    UG.UserID,
    UG.WaterIntakeGoal,
    COALESCE(TotalWaterIntakeToday, 0) AS TotalWaterIntakeToday,
    (UG.WaterIntakeGoal - COALESCE(TotalWaterIntakeToday, 0)) AS AdditionalWaterNeeded
FROM 
    UserGoal UG
LEFT JOIN 
    (
        SELECT 
            UserID,
            COALESCE(SUM(WaterIntake), 0) AS TotalWaterIntakeToday
        FROM 
            DailyActivity
        WHERE 
            UserID = 2
            AND Date = CURRENT_DATE
        GROUP BY 
            UserID
    ) TWI ON UG.UserID = TWI.UserID;
