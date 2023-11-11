-- Insert data into ExerciseTypes Table
INSERT INTO ExerciseTypes (TypeExerciseName, TypeExerciseDescription) VALUES
    ('Cardiovascular', 'Activities that increase heart rate'),
    ('Strength Training', 'Exercises focused on muscle building'),
    ('HIIT', 'High Intensity Interval Training'),
    ('Circuit Training', 'Series of exercises performed in rotation with minimal breaks');

-- Insert data into TrainingGoal Table (Bulk, Cut, Maintain)
INSERT INTO TrainingGoal (GoalName, NetCaloriesGoal) VALUES
    ('Bulk', 400),
    ('Cut', -400),
    ('Maintain', 0);

-- Insert data into WorkoutsTable
INSERT INTO WorkoutsTable (WorkoutName, AvgCaloriesBurnedPerMinute, WorkoutDescription, WorkoutVideoURL) VALUES
    ('Running', 7.5, 'Jogging or running outdoors or on a treadmill.', 'https://example.com/running_video'),
    ('Cycling', 6.0, 'Riding a bicycle, either outdoors or on a stationary bike.', 'https://example.com/cycling_video'),
    ('Swimming', 8.0, 'Swimming laps in a pool or open water.', 'https://example.com/swimming_video'),
    ('Jump Rope', 10.0, 'Skipping rope for cardiovascular fitness.', 'https://example.com/jump_rope_video'),
    ('Rowing', 6.5, 'Using a rowing machine for a full-body workout.', 'https://example.com/rowing_video'),
    ('Bench Press', 5.0, 'Lifting weights while lying on a bench.', 'https://example.com/bench_press_video'),
    ('Squat', 4.8, 'A compound exercise that targets the lower body.', 'https://example.com/squat_video'),
    ('Deadlift', 6.2, 'Lifting a barbell from the ground to hip level.', 'https://example.com/deadlift_video'),
    ('Pull-Ups', 5.5, 'Using a pull-up bar to work the upper body.', 'https://example.com/pull_ups_video'),
    ('Dumbbell Curls', 4.5, 'Lifting dumbbells to work the biceps.', 'https://example.com/dumbbell_curls_video'),
    ('Burpees', 9.0, 'A full-body exercise involving a squat, push-up, and jump.', 'https://example.com/burpees_video'),
    ('Jumping Lunges', 8.5, 'Alternating lunges with explosive jumps.', 'https://example.com/jumping_lunges_video'),
    ('Push-Ups', 6.0, 'Performing a set of push-ups.', 'https://example.com/push_ups_video'),
    ('Leg Raises', 5.5, 'Lying on your back and raising your legs off the ground.', 'https://example.com/leg_raises_video');

-- Insert data into WorkoutExerciseTypesJunction
-- Example junction data based on exercise categories
INSERT INTO WorkoutExerciseTypesJunction (WorkoutID, TypeExerciseID) VALUES
    (1, 1),  -- Running (Cardiovascular)
    (2, 1),  -- Cycling (Cardiovascular)
    (3, 1),  -- Swimming (Cardiovascular)
    (4, 1),  -- Jump Rope (Cardiovascular)
    (5, 1),  -- Rowing (Cardiovascular)
    (6, 2),  -- Bench Press (Strength Training)
    (7, 2),  -- Squat (Strength Training)
    (8, 2),  -- Deadlift (Strength Training)
    (9, 2),  -- Pull-Ups (Strength Training)
    (10, 2), -- Dumbbell Curls (Strength Training)
    (11, 3), -- Burpees (HIIT)
    (12, 3), -- Jumping Lunges (HIIT)
    (13, 4), -- Push-Ups (Circuit Training)
    (14, 4); -- Leg Raises (Circuit Training)
