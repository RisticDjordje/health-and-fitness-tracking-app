-- retrieves the sleep data for a user over the past 7 days

SELECT 
    UserID,
    SleepStart,
    SleepEnd,
    SleepDuration
FROM 
    DailySleep
WHERE 
    UserID = 5 AND
    Date(SleepStart) >= Date('now', '-7 days')
ORDER BY 
    SleepStart;
