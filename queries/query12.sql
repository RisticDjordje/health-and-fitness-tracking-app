-- Satisfied daily sleep hours goal streak 

WITH DailyTotals AS (
    SELECT 
        UserID,
        DATE(SleepStart) AS Date,
        SUM(SleepDuration) AS TotalSleepDuration
    FROM 
        DailySleep
    WHERE 
        UserID = 8 -- Replace with the actual user ID
    GROUP BY 
        UserID, Date
),
Streaks AS (
    SELECT 
        DT.UserID,
        DT.Date,
        DT.TotalSleepDuration,
        SG.SleepGoal,
        JULIANDAY(DT.Date) - JULIANDAY(IFNULL(PREV.Date, DT.Date)) AS DaysSincePrevious
    FROM 
        DailyTotals DT
    JOIN 
        SleepGoal SG ON DT.UserID = SG.UserID
    LEFT JOIN 
        DailyTotals PREV ON DT.UserID = PREV.UserID AND DATE(PREV.Date) = DATE(DT.Date, '-1 day')
    WHERE 
        DT.TotalSleepDuration >= SG.SleepGoal
)
SELECT 
    COUNT(*) AS CurrentStreak
FROM 
    Streaks
WHERE 
    UserID = 8 AND DaysSincePrevious = 1;
