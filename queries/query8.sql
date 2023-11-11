-- Calculate the average 7-day sleeping hours for a specific user and 
WITH UserSleepGoal AS (
    SELECT 
        U.UserID,
        SG.SleepGoal AS SleepGoalHours
    FROM 
        Users U
    JOIN 
        SleepGoal SG ON U.UserID = SG.UserID
    WHERE 
        U.UserID = 2
),
AvgSleep AS (
    SELECT 
        UserID,
        AVG(SleepDuration) AS AvgSleepDuration
    FROM 
        DailySleep
    WHERE 
        UserID = 2
        AND Date(SleepStart) >= Date('now', '-7 days')
    GROUP BY 
        UserID
)
SELECT 
    USG.UserID,
    USG.SleepGoalHours,
    COALESCE(ASD.AvgSleepDuration, 0) AS AverageSleepDuration,
    CASE
        WHEN ASD.AvgSleepDuration < USG.SleepGoalHours THEN USG.SleepGoalHours - ASD.AvgSleepDuration
        ELSE ASD.AvgSleepDuration - USG.SleepGoalHours
    END AS SleepSuggestion
FROM 
    UserSleepGoal USG
LEFT JOIN 
    AvgSleep ASD ON USG.UserID = ASD.UserID;
