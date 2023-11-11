-- Returns the calories the user should consume or burn today to meet their training goal

SELECT
    U.UserID,
    TG.NetCaloriesGoal,
    COALESCE(DA.NetCalories, 0) AS CurrentNetCalories, -- COALESCE is used to replace NULL values with 0
    (TG.NetCaloriesGoal - COALESCE(DA.NetCalories, 0)) AS CaloriesToConsumeOrBurn
FROM
    UserTrainingGoal UTG
    JOIN TrainingGoal TG ON UTG.GoalID = TG.GoalID
    JOIN Users U ON UTG.UserID = U.UserID
    LEFT JOIN (
        SELECT
            *
        FROM
            DailyActivity
        WHERE
            Date = CURRENT_DATE
    ) DA ON U.UserID = DA.UserID
WHERE
    U.UserID = 3;