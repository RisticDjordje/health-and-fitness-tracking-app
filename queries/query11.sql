-- Satisfied daily water intake goal streak 

WITH DailyTotals AS (
    SELECT 
        UserID,
        DATE(WaterIntakeDatetime) AS Date,
        SUM(WaterIntakeAmount) AS TotalWaterIntake
    FROM 
        DailyWaterIntake
    WHERE 
        UserID = 2 -- Replace with the actual user ID
    GROUP BY 
        UserID, Date
),
Streaks AS (
    SELECT 
        DT.UserID,
        DT.Date,
        DT.TotalWaterIntake,
        WG.WaterIntakeGoal,
        JULIANDAY(DT.Date) - JULIANDAY(IFNULL(PREV.Date, DT.Date)) AS DaysSincePrevious
    FROM 
        DailyTotals DT
    JOIN 
        WaterIntakeGoal WG ON DT.UserID = WG.UserID
    LEFT JOIN 
        DailyTotals PREV ON DT.UserID = PREV.UserID AND DATE(PREV.Date) = DATE(DT.Date, '-1 day')
    WHERE 
        DT.TotalWaterIntake >= WG.WaterIntakeGoal
)
SELECT 
    COUNT(*) AS CurrentStreak
FROM 
    Streaks
WHERE 
    UserID = 2 AND DaysSincePrevious = 1;
