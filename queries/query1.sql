-- For User X=2, find out how many more calories they should consume or burn
-- to reach their daily net calorie goal, which depends on their TrainingGoal.

SELECT NetCalories FROM DailyActivity WHERE UserID = 2;

-- Join the TrainingGoal table with UseTrainingGoal table to find out the NetCalori
SELECT GoalID FROM UserTrainingGoal WHERE UserID = 2;
