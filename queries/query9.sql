-- Retrieve Water Intake, Sleep, Weight, and BMI for a Given User Today
SELECT
    DA.UserID,
    DA.Date AS Date,
    COALESCE(DA.WaterIntake, 0) AS "Water Intake (liters)",
    COALESCE(DS.SleepDuration, 0) AS "Sleep (hours)",
    UH.Weight AS "Weight (kg)",
    CASE
        WHEN UH.Height IS NOT NULL AND UH.Weight IS NOT NULL
        THEN UH.Weight / ((UH.Height / 100) * (UH.Height / 100))
        ELSE NULL
    END AS "BMI"
FROM Users U
LEFT JOIN DailySleep DS ON U.UserID = DS.UserID AND DS.SleepStart >= DATE('now', 'localtime') AND DS.SleepStart < DATE('now', 'localtime', '+1 day')
LEFT JOIN UserHealth UH ON U.UserID = UH.UserID
LEFT JOIN DailyActivity DA ON U.UserID = DA.UserID AND DA.Date = DATE('now', 'localtime')
WHERE U.UserID = 1
