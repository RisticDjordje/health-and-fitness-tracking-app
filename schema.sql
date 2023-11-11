-- PRIMARY USER INFORMATION TABLES
CREATE TABLE
    Users (
        UserID INTEGER PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        DateOfBirth DATE,
        Sex VARCHAR(10)
    );

-- AUTHENTICATION TABLES
CREATE TABLE
    Authentication (
        UserID INTEGER,
        Username VARCHAR(50) UNIQUE NOT NULL,
        HashedPassword TEXT NOT NULL,
        Email VARCHAR(100) UNIQUE NOT NULL,
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

-- USER HEALTH TABLE
CREATE TABLE
    UserHealth (
        UserID INTEGER,
        Height REAL NOT NULL, -- Height in cm
        Weight REAL NOT NULL, -- Weight in kg
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

-- SLEEP TABLES
-- User daily sleep goal table
CREATE TABLE
    SleepGoal (
        SleepGoalID INTEGER PRIMARY KEY,
        UserID INTEGER,
        SleepGoal REAL NOT NULL, -- Sleep goal in hours
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

-- Daily sleep tracking table
CREATE TABLE
    DailySleep (
        SleepID INTEGER PRIMARY KEY,
        UserID INTEGER,
        SleepStart DATETIME NOT NULL,
        SleepEnd DATETIME NOT NULL,
        SleepDuration REAL NOT NULL, -- Sleep duration in hours: SleepEnd - SleepStart BE CAREFUL ABOUT THE DATE CHANGE
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

-- WATER INTAKE TABLES
CREATE TABLE
    WaterIntakeGoal (
        WaterIntakeGoalID INTEGER PRIMARY KEY,
        UserID INTEGER,
        WaterIntakeGoal REAL NOT NULL DEFAULT 3, -- Water intake goal in liters
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

CREATE TABLE
    DailyWaterIntake (
        WaterIntakeID INTEGER PRIMARY KEY,
        UserID INTEGER,
        WaterIntakeDatetime DATETIME NOT NULL,
        WaterIntakeAmount REAL NOT NULL DEFAULT 0, -- Water intake amount in leters
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

-- NUTRITION TABLES
-- Insert meal had in a day table
CREATE TABLE
    DailyMeals (
        MealID INTEGER PRIMARY KEY,
        UserID INTEGER,
        MealDate DATETIME NOT NULL,
        MealName VARCHAR(255) NOT NULL,
        Calories REAL NOT NULL,
        MealDescription TEXT,
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
    );

---- TRAINING TABLES
-- Goals Table (Bulking, Cutting, Maintain)
CREATE TABLE
    TrainingGoal (
        GoalID INTEGER PRIMARY KEY,
        GoalName VARCHAR(255) NOT NULL UNIQUE,
        NetCaloriesGoal REAL NOT NULL -- Net calorie change in kcal/day
    );

-- UserTrainingGoal Table (junction table for Users and Goals)
CREATE TABLE
    UserTrainingGoal (
        UserID INTEGER,
        GoalID INTEGER,
        FOREIGN KEY (UserID) REFERENCES Users (UserID),
        FOREIGN KEY (GoalID) REFERENCES TrainingGoal (GoalID),
        UNIQUE (UserID, GoalID)
    );

-- ExerciseTypes Table (Cardiovascular, Strength Training, HIIT, Circuit Training)
CREATE TABLE
    ExerciseTypes (
        TypeExerciseID INTEGER PRIMARY KEY,
        TypeExerciseName VARCHAR(255) NOT NULL UNIQUE,
        TypeExerciseDescription TEXT
    );

-- Workouts Table (Running, Pushups, etc.)
CREATE TABLE
    WorkoutsTable (
        WorkoutID INTEGER PRIMARY KEY,
        WorkoutName VARCHAR(255) NOT NULL UNIQUE,
        AvgCaloriesBurnedPerMinute REAL NOT NULL,
        WorkoutDescription TEXT,
        WorkoutVideoURL TEXT
    );

-- JUNCTION TABLE FOR WORKOUTS AND EXERCISE TYPES (connects running with cardiovascular, etc.)
CREATE TABLE
    WorkoutExerciseTypesJunction (
        WorkoutID INTEGER,
        TypeExerciseID INTEGER,
        FOREIGN KEY (WorkoutID) REFERENCES WorkoutsTable (WorkoutID),
        FOREIGN KEY (TypeExerciseID) REFERENCES ExerciseTypes (TypeExerciseID),
        UNIQUE (WorkoutID, TypeExerciseID)
    );

-- UserWorkouts Table
CREATE TABLE
    UserWorkouts (
        UserID INTEGER,
        WorkoutID INTEGER,  -- WorkoutID from WorkoutsTable (Running, Pushups, etc.)
        StartTime DATETIME NOT NULL,
        EndTime DATETIME NOT NULL, -- what happens if workout spans multiple days? add it to the day it started 
        Duration REAL NOT NULL, -- Duration in minutes (EndTime - StartTime)
        CaloriesBurned REAL NOT NULL, -- AvgCaloriesBurnedPerMinute * Duration
        FOREIGN KEY (UserID) REFERENCES Users (UserID),
        FOREIGN KEY (WorkoutID) REFERENCES WorkoutsTable (WorkoutID),
        UNIQUE (UserID, WorkoutID, StartTime)
    );

CREATE TABLE
    DailyActivity (
        ActivityID INTEGER PRIMARY KEY,
        UserID INTEGER,
        Date DATE NOT NULL,
        WaterIntake REAL DEFAULT 0,
        TotalCaloriesBurned REAL DEFAULT 0,
        TotalCaloriesConsumed REAL DEFAULT 0,
        NetCalories REAL, -- TotalCaloriesConsumed - TotalCaloriesBurned - BMR
        FOREIGN KEY (UserID) REFERENCES Users (UserID)
        UNIQUE (UserID, Date)
    );