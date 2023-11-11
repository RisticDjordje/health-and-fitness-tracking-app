-- Current Active Training Streak
WITH OrderedWorkouts AS (
    SELECT 
        UserID, 
        DATE(StartTime) AS WorkoutDate,
        ROW_NUMBER() OVER (PARTITION BY UserID ORDER BY DATE(StartTime) DESC) AS RowNum
    FROM 
        UserWorkouts
    WHERE 
        UserID = 3 -- Replace with the actual user ID
),
Streaks AS (
    SELECT 
        OW1.UserID,
        OW1.WorkoutDate,
        JULIANDAY(OW1.WorkoutDate) - JULIANDAY(IFNULL(OW2.WorkoutDate, OW1.WorkoutDate)) AS DaysSinceNextWorkout
    FROM 
        OrderedWorkouts OW1
    LEFT JOIN 
        OrderedWorkouts OW2 ON OW1.UserID = OW2.UserID AND OW1.RowNum = OW2.RowNum - 1
)
SELECT 
    COUNT(*) AS CurrentStreak
FROM 
    Streaks
WHERE 
    UserID = 2 AND DaysSinceNextWorkout = 1;
