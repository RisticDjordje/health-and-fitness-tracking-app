import unittest
import sqlite3
from io import StringIO

class TestDatabase(unittest.TestCase):
    def setUp(self):
        # Create an in-memory database for testing
        self.conn = sqlite3.connect(':memory:')
        self.cursor = self.conn.cursor()

        # Read and execute the schema SQL script
        with open('schema.sql', 'r') as schema_file:
            schema_script = schema_file.read()
            self.cursor.executescript(schema_script)

    def tearDown(self):
        # Close the database connection after each test
        self.conn.close()

    def test_insert_user(self):
        # Test data
        user_data = (1, 'John', 'Doe', '1990-01-01', 'Male')

        # Insert data into Users table
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (?, ?, ?, ?, ?)', user_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM Users WHERE UserID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, user_data)

    def test_unique_username_constraint(self):
        # Insert test data
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')
        self.cursor.execute('INSERT INTO Authentication (UserID, Username, HashedPassword, Email) VALUES (1, "john_doe", "hashed_password", "john@example.com")')

        # Attempt to insert a duplicate username
        with self.assertRaises(sqlite3.IntegrityError):
            self.cursor.execute('INSERT INTO Authentication (UserID, Username, HashedPassword, Email) VALUES (2, "john_doe", "another_password", "jane@example.com")')
    
    def test_insert_user_health(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Test data for UserHealth
        user_health_data = (1, 180.0, 70.0)  # UserID, Height, Weight

        # Insert data into UserHealth table
        self.cursor.execute('INSERT INTO UserHealth (UserID, Height, Weight) VALUES (?, ?, ?)', user_health_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM UserHealth WHERE UserID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, user_health_data)

    def test_insert_sleep_data(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Test data for DailySleep
        sleep_data = (1, 1, '2023-01-01 22:00:00', '2023-01-02 06:00:00', 8.0)  # SleepID, UserID, SleepStart, SleepEnd, SleepDuration

        # Insert data into DailySleep table
        self.cursor.execute('INSERT INTO DailySleep (SleepID, UserID, SleepStart, SleepEnd, SleepDuration) VALUES (?, ?, ?, ?, ?)', sleep_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM DailySleep WHERE SleepID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, sleep_data)

    def test_water_intake_goal_default_value(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Insert data into WaterIntakeGoal table without specifying WaterIntakeGoal
        self.cursor.execute('INSERT INTO WaterIntakeGoal (WaterIntakeGoalID, UserID) VALUES (1, 1)')

        # Fetch the inserted data
        self.cursor.execute('SELECT WaterIntakeGoal FROM WaterIntakeGoal WHERE WaterIntakeGoalID = 1')
        result = self.cursor.fetchone()

        # Assert that the default value for WaterIntakeGoal is used
        self.assertEqual(result[0], 3.0)

    def test_unique_workout_per_user_and_start_time(self):
        # Insert test data
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')
        self.cursor.execute('INSERT INTO WorkoutsTable (WorkoutID, WorkoutName, AvgCaloriesBurnedPerMinute) VALUES (1, "Running", 10)')

        # Insert first workout record
        self.cursor.execute('INSERT INTO UserWorkouts (UserID, WorkoutID, StartTime, EndTime, Duration, CaloriesBurned) VALUES (1, 1, "2023-01-01 07:00:00", "2023-01-01 07:30:00", 30, 300)')

        # Attempt to insert a duplicate workout record for the same user and start time
        with self.assertRaises(sqlite3.IntegrityError):
            self.cursor.execute('INSERT INTO UserWorkouts (UserID, WorkoutID, StartTime, EndTime, Duration, CaloriesBurned) VALUES (1, 1, "2023-01-01 07:00:00", "2023-01-01 07:45:00", 45, 450)')
    
    def test_insert_daily_meal(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Test data for DailyMeals
        meal_data = (1, 1, '2023-01-01 12:00:00', 'Lunch', 600, 'Chicken salad')

        # Insert data into DailyMeals table
        self.cursor.execute('INSERT INTO DailyMeals (MealID, UserID, MealDate, MealName, Calories, MealDescription) VALUES (?, ?, ?, ?, ?, ?)', meal_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM DailyMeals WHERE MealID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, meal_data)

    def test_training_goal_insertion(self):
        # Test data for TrainingGoal
        goal_data = (1, 'Bulking', 500)

        # Insert data into TrainingGoal table
        self.cursor.execute('INSERT INTO TrainingGoal (GoalID, GoalName, NetCaloriesGoal) VALUES (?, ?, ?)', goal_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM TrainingGoal WHERE GoalID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, goal_data)

    def test_unique_exercise_type(self):
        # Test data for ExerciseTypes
        exercise_type_data = (1, 'Cardiovascular', 'Activities that increase heart rate')

        # Insert first exercise type
        self.cursor.execute('INSERT INTO ExerciseTypes (TypeExerciseID, TypeExerciseName, TypeExerciseDescription) VALUES (?, ?, ?)', exercise_type_data)

        # Attempt to insert a duplicate exercise type
        with self.assertRaises(sqlite3.IntegrityError):
            self.cursor.execute('INSERT INTO ExerciseTypes (TypeExerciseID, TypeExerciseName, TypeExerciseDescription) VALUES (2, "Cardiovascular", "Similar activities")')

    def test_daily_activity_insertion(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Test data for DailyActivity
        activity_data = (1, 1, '2023-01-01', 2.5, 500, 2000, 1500)

        # Insert data into DailyActivity table
        self.cursor.execute('INSERT INTO DailyActivity (ActivityID, UserID, Date, WaterIntake, TotalCaloriesBurned, TotalCaloriesConsumed, NetCalories) VALUES (?, ?, ?, ?, ?, ?, ?)', activity_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM DailyActivity WHERE ActivityID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, activity_data)

    def test_user_training_goal_association(self):
        # Insert test user and training goal
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')
        self.cursor.execute('INSERT INTO TrainingGoal (GoalID, GoalName, NetCaloriesGoal) VALUES (1, "Bulking", 500)')

        # Test data for UserTrainingGoal
        user_training_goal_data = (1, 1)

        # Insert data into UserTrainingGoal table
        self.cursor.execute('INSERT INTO UserTrainingGoal (UserID, GoalID) VALUES (?, ?)', user_training_goal_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM UserTrainingGoal WHERE UserID = 1 AND GoalID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, user_training_goal_data)

    def test_insert_workout(self):
        # Test data for WorkoutsTable
        workout_data = (1, 'Running', 10.0, 'Outdoor running', 'http://example.com/running')

        # Insert data into WorkoutsTable
        self.cursor.execute('INSERT INTO WorkoutsTable (WorkoutID, WorkoutName, AvgCaloriesBurnedPerMinute, WorkoutDescription, WorkoutVideoURL) VALUES (?, ?, ?, ?, ?)', workout_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM WorkoutsTable WHERE WorkoutID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, workout_data)

    def test_insert_workout_exercise_type_junction(self):
        # Insert test data for ExerciseTypes and WorkoutsTable
        self.cursor.execute('INSERT INTO ExerciseTypes (TypeExerciseID, TypeExerciseName) VALUES (1, "Cardiovascular")')
        self.cursor.execute('INSERT INTO WorkoutsTable (WorkoutID, WorkoutName, AvgCaloriesBurnedPerMinute) VALUES (1, "Running", 10)')

        # Test data for WorkoutExerciseTypesJunction
        junction_data = (1, 1)

        # Insert data into WorkoutExerciseTypesJunction
        self.cursor.execute('INSERT INTO WorkoutExerciseTypesJunction (WorkoutID, TypeExerciseID) VALUES (?, ?)', junction_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM WorkoutExerciseTypesJunction WHERE WorkoutID = 1 AND TypeExerciseID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, junction_data)

    def test_insert_daily_water_intake(self):
        # Insert test user
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')

        # Test data for DailyWaterIntake
        water_intake_data = (1, 1, '2023-01-01 08:00:00', 0.5)

        # Insert data into DailyWaterIntake table
        self.cursor.execute('INSERT INTO DailyWaterIntake (WaterIntakeID, UserID, WaterIntakeDatetime, WaterIntakeAmount) VALUES (?, ?, ?, ?)', water_intake_data)

        # Fetch the inserted data
        self.cursor.execute('SELECT * FROM DailyWaterIntake WHERE WaterIntakeID = 1')
        result = self.cursor.fetchone()

        # Assert that the data was inserted correctly
        self.assertEqual(result, water_intake_data)

    def test_update_user_weight(self):
        # Insert test user and user health data
        self.cursor.execute('INSERT INTO Users (UserID, FirstName, LastName, DateOfBirth, Sex) VALUES (1, "John", "Doe", "1990-01-01", "Male")')
        self.cursor.execute('INSERT INTO UserHealth (UserID, Height, Weight) VALUES (1, 180.0, 70.0)')

        # Update user weight
        self.cursor.execute('UPDATE UserHealth SET Weight = 75.0 WHERE UserID = 1')

        # Fetch the updated data
        self.cursor.execute('SELECT Weight FROM UserHealth WHERE UserID = 1')
        result = self.cursor.fetchone()

        # Assert that the weight was updated correctly
        self.assertEqual(result[0], 75.0)


if __name__ == '__main__':
    unittest.main()

