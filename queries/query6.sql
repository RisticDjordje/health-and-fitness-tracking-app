-- Calculate and return the average SleepDuration for the past 7 days for UserID = 5
SELECT 
    AVG(SleepDuration) AS AvgSleepDuration
FROM 
    DailySleep
WHERE 
    UserID = 5 AND
    Date(SleepStart) >= Date('now', '-7 days');