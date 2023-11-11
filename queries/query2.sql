-- For the user's input of their training goal (HIIT, Cardiovascular), 
-- we show them all excercises from that type

SELECT 
    WT.WorkoutName, 
    WT.AvgCaloriesBurnedPerMinute
FROM 
    WorkoutsTable WT
JOIN 
    WorkoutExerciseTypesJunction WETJ ON WT.WorkoutID = WETJ.WorkoutID
JOIN 
    ExerciseTypes ET ON WETJ.TypeExerciseID = ET.TypeExerciseID
WHERE 
    ET.TypeExerciseName = 'Cardiovascular' -- Replace 'HIIT' with the desired exercise type (e.g., 'Cardiovascular')
ORDER BY 
    WT.AvgCaloriesBurnedPerMinute DESC;
