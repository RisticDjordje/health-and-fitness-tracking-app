# Health and Fitness Tracking App

## Overview

Welcome to our Health and Fitness Tracking App, a comprehensive solution designed to help users monitor and achieve their health and fitness goals. This application seamlessly integrates various aspects of health management, including sleep tracking, water intake, workout logging, nutrition monitoring, and personalized fitness recommendations. Built with a focus on user experience, data integrity, and robust functionality, our app provides an intuitive platform for users to track their daily activities, set and achieve fitness goals, and maintain a healthy lifestyle.

Key features of the app include:
- **Sleep Tracking:** Monitor and analyze sleep patterns for improved rest.
- **Water Intake Recording:** Keep track of daily hydration levels.
- **Workout Logging:** Log workouts and track progress over time.
- **Nutrition Monitoring:** Record and manage daily nutritional intake.
- **Personalized Fitness Recommendations:** Receive tailored advice based on individual health metrics and goals.

Our app is backed by a well-structured database, ensuring data normalization, integrity, and efficient query processing. With comprehensive testing and robust error handling mechanisms, we ensure a reliable and user-friendly experience. Dive into a detailed exploration of our app's functionalities, setup instructions, and the underlying database structure in the sections below.

---
# Table of Contents
1. [Overview](#overview)
2. [Data Collection Process and Important Concepts](#data-collection-process-and-important-concepts)
   - [BMR Calculation](#bmr-calculation)
   - [Setting Goals](#setting-goals)
   - [Explanation of Key Processes](#explanation-of-key-processes)
3. [Core Functionalities](#core-functionalities)
   - [Sleep Tracking](#sleep-tracking)
   - [Water Intake Recording](#water-intake-recording)
   - [Workout Logging](#workout-logging)
   - [Nutrition Monitoring](#nutrition-monitoring)
   - [Personalized Fitness Recommendations](#personalized-fitness-recommendations)
4. [Dashboard and Analytics](#dashboard-and-analytics)
5. [Installation and Setup](#installation-and-setup)
6. [File Structure](#file-structure)
7. [SQL Queries Description](#sql-queries-description)
8. [Comprehensive and Detailed Testing Approach](#comprehensive-and-detailed-testing-approach)
9. [Robust Database Testing with Transactions and Exception Handling](#robust-database-testing-with-transactions-and-exception-handling)
10. [Data Normalization in Health and Fitness Tracking App](#data-normalization-in-health-and-fitness-tracking-app)


---

## Data collection process and important concepts
Upon registration, users are required to provide essential demographics:

- **Email, Username, First Name, Last Name:** Basic identification details.
- **Date of Birth:** Used for age calculation.
- **Sex:** A critical demographic for various calculations.
- **Height and Weight:** Key metrics for health tracking. Height is relatively static, whereas weight can fluctuate.


Using this information we can calcualte the *Basal Metabolic Rate (BMR)*. To elaborate this, people burn a specific amount of calories in a day through activities such as breathing, sleeping, etc. This average amount of calories burned in a day is calculated through the BMR formulas:

#### BMR Calculation
The BMR is calculated using the following formulas:

- For Men:
  ```
  88.362 + (13.397 × weight in kg) + (4.799 × height in cm) - (5.677 × age in years)
  ```
- For Women:
  ```
  BMR = 447.593 + (9.247 × weight in kg) + (3.098 × height in cm) - (4.330 × age in years)
  ```

This is a critical metric for determining the number of calories a user should consume in a day. The app will use this information to provide personalized fitness recommendations.

### Setting Goals

The next step in the registration process is setting goals. Here, users define their fitness goals through the following parameters:

- **Weight Goal:** Options include gain (bulk), lose (cut), or maintain.
- **Weight Goal Amount:** Specified in kilograms.
- **Average Night Sleep:** Measured in hours.
- **Average Daily Water Intake:** Recommendations are provided based on sex and weight.

To better understand these goals we need to understand some key processes.

#### Explanation of key processes
Besides BMR, another way people burn calories is through excercise and the amount of calories burned depends on the type of excercise they do and the duration of the excercise. For example, running burns more calories than walking. On the other hand, calories are replenished through food. The amount of calories depends on the type of food (protein, fat, carbohydrates, etc.) eaten and the quanityt. For example, a burger has more calories than a salad. Knowing this gives us enough information to calculate **the net calories**.

```
net calories = calories taken in by food - calories burned by excercise - BMR calories burned.
``` 

1. Now, if the user wants to **lose weight / cut**, they have to be in a **caloric deficit**. The usual recommended caloric deficit is 400 calories. This is the value that the user should be aspiring to achieve. 
2. If the user wants to **gain weight / bulk**, they have to be in a **caloric surplus**. The usual recommended caloric surplus is 400 calories (this is the NetCalorieChange for this goal). This is the value that the user should be aspiring to achieve.
3. If the user wants to maintain weight, they have to be in a **caloric balance**. This means that the net calories should be around 0.

Depending on the goal set and the users goal, the app will provide personalized fitness recommendations.


## Core Functionalities
The app offers five main features:

### 1. Sleep Tracking
Users record their sleep duration by indicating when they go to bed and wake up. The user will have a component in the app where they will be able to click when they are going to sleep and then when they wake up. This will measure the duration of their sleep. 

On the dashboard they will see how much sleep they have had today. They will see the average sleep amount over the last 7 days too and a graph of sleep over the last 7 days.

### 2. Water Intake Recording
For record water, the user will have a component in the app where they will be able to click how much water they drank today since last opening the app. They will be given options such as 1L, 0.5L, and a custom amount. This will increment the water they have drunk for the day. 

On the main dashboard, they will see how much water they have had today and how much more they should drink. The user will also be able to see a graph of their water intake over the last 7 days and the average water intake over the last 7 days too.

### 3. Workout Logging
For logging physical activity, the user will be able to select a workout type from a list of options. They will be able to click start workout and also end workout meaning the system will count the duration of the workout. Since each workout type will have an estimated calorie burn per minute, the system will be able to calculate the total calories burned. This is a base version and is an approximation that will be improved upon in the future.

### 4. Nutrition Monitoring
For logging nutrition the user will have a component in the app where they will be able to track what they ate in a day. They will be able to write what they ate, leave a note for a category and, most importantly, input the calories they ate. The system will record how many calories they have eaten today and also send the time and date at which the food has been eaten. In future versions, the calory input could be automated by scanning the barcode of the food item or scanning the food item itself or by using a database of food items and their calories.

### 5. Personalized Fitness Recommendations
As explained above, the app will at all times tell the users:
1. How many more calories they should intake or burn to reach their training goal (bulk, cut, or maintain).
2. How many more liters of water they should drink today to reach their water goal.
3. Give them recommendation for which exercices they should based on what type of workout they want to do (Cardiovascular, Strength, HIIT, etc.)
4. How many more hours of sleep they should be getting a week to reach their sleep goal.

## Dashboard and Analytics
The dashboard queries things to display key metrics like:
- **Net Calories:** The difference between calories consumed and calories burned.
- **Water Intake:** The amount of water consumed in liters.
- **Sleep:** The amount of sleep in hours.
- **Weight:** The user's weight in kilograms.
- **BMI:** The user's body mass index.
- **How many more calories they should intake or burn to reach their training goal (bulk, cut, or maintain).**
- **How many more liters of water they should drink today to reach their water goal.**
- **Give them recommendation for which exercices they should based on what type of workout they want to do (Cardiovascular, Strength, HIIT, etc.)**
- **How many more hours of sleep they should be getting a week to reach their sleep goal.**
- **Training streak** (how many consecutive days in a row they have worked out)
- **Water streak** (how many consecutive days in a row they have drank enough water)
- **Sleep streak** (how many consecutive days in a row they have slept enough)

# Installation and setup

To run this code:

Create a (conda ideally) virtual environment and install the requirements:

```bash
conda create -n myenv python=3.11
conda activate myenv
pip install -r requirements.txt
```

To run the main code, including the queries just run
  
  ```bash
  python main.py
  ```

To run the tests, run

  ```bash
  python -m unittest discover
  ```

## File Structure
- `README.md` - This file.
- `base_data.sql` - Base data for the application.
- `fakedata.py` - Script to generate fake data.
- `main.py` - Main application script.
- `queries/` - Directory containing SQL queries.
  - `query1.sql` - Calculates calories to consume or burn for training goals.
  - `query2.sql` - Lists exercises based on workout type.
  - `query3.sql` - Retrieves 7-day sleep data.
  - `query4.sql` - Aggregates daily user data over 7 days.
  - `query5.sql` - Calculates 7-day averages for user metrics.
  - `query6.sql` - Calculates average sleep duration over 7 days.
  - `query7.sql` - Determines additional water needed to meet daily goal.
  - `query8.sql` - Calculates average 7-day sleeping hours and suggestions.
  - `query9.sql` - Retrieves current day's water intake, sleep, weight, and BMI.
  - `query10.sql` - Tracks current active training streak.
  - `query11.sql` - Tracks water intake goal streak.
  - `query12.sql` - Tracks sleep hours goal streak.
- `schema.sql` - Database schema.
- `test.py` - Script for running tests.

## SQL Queries Description
Each SQL query in the `queries` directory serves a specific purpose:

#### `query1.sql`
Calculates the calories a user should consume or burn today to meet their training goal.

#### `query2.sql`
Lists exercises for the user's chosen workout type (e.g., Cardiovascular, HIIT).

#### `query3.sql`
Retrieves the user's sleep data for the last 7 days.

#### `query4.sql`
Aggregates daily user data over the past 7 days, including water intake, calories consumed and burned.

#### `query5.sql`
Calculates 7-day averages for water intake, calories consumed, calories burned, and net calories.

#### `query6.sql`
Calculates the average sleep duration for a user over the past 7 days.

#### `query7.sql`
Determines how much more water a user needs to drink today to reach their daily goal.

#### `query8.sql`
Calculates the average sleeping hours over 7 days for a user and provides sleep suggestions.

#### `query9.sql`
Retrieves today's water intake, sleep duration, weight, and BMI for a given user.

#### `query10.sql`
Tracks the current active training streak of a user.

#### `query11.sql`
Tracks the streak of meeting the daily water intake goal.

#### `query12.sql`
Tracks the streak of meeting the daily sleep hours goal.



## Comprehensive and Detailed Testing Approach

### Overview
Our health and fitness tracking app employs a meticulous and thorough testing strategy, as exemplified by the `TestDatabase` class. This class, written in Python and utilizing the `unittest` framework, demonstrates our commitment to ensuring the reliability and accuracy of the application's interaction with the database.

### Key Features of the `TestDatabase` Class

#### 1. **In-Memory Database Testing**
   - The tests are conducted using an in-memory SQLite database, allowing for fast and isolated testing environments.
   - This approach ensures that tests do not interfere with each other or with a persistent database, maintaining test integrity.

#### 2. **Schema Script Execution**
   - Each test begins by reading and executing the schema SQL script, ensuring that the database structure is consistent with the application's requirements.

#### 3. **Comprehensive Test Cases**
   - **User Data Insertion:** Tests validate the correct insertion of user data into the database, ensuring data integrity.
   - **Unique Username Constraint:** The application's enforcement of unique usernames is tested, a crucial aspect for user authentication.
   - **Health Data Management:** Tests cover the insertion of user health data, including height, weight, and sleep data, ensuring comprehensive health tracking.
   - **Water Intake and Workout Data:** The application's ability to handle water intake goals and workout data is thoroughly tested.
   - **Meal and Activity Tracking:** Tests ensure that meal and daily activity data are correctly managed by the application.
   - **Training Goals and Exercise Types:** The system's handling of training goals and exercise types is validated through dedicated test cases.

#### 4. **Error Handling and Constraints**
   - The tests include scenarios that trigger database constraints (like unique constraints), ensuring the application handles such cases gracefully.
   - This approach is vital for maintaining data consistency and preventing invalid data entries.

#### 5. **Data Update and Retrieval**
   - Tests are not limited to data insertion but also include scenarios for data updating and retrieval, covering a wide range of database operations.
   - This ensures that the application can not only store but also correctly retrieve and update user data.


## Robust Database Testing with Transactions and Exception Handling

### Overview
Our health and fitness tracking app ensures the integrity and reliability of database operations through the strategic use of transactions, exception handling, and enforcing foreign key constraints. This approach is consistently applied across various database interactions, including table creation, data insertion, and query execution.

### Key Aspects of Our Approach

#### 1. **Enforcing Referential Integrity with Foreign Key Constraints**
   - **PRAGMA foreign_keys = ON:** We ensure referential integrity in our SQLite database by enabling foreign key constraints. This is crucial for maintaining the relational integrity of the data and preventing orphan records.

#### 2. **Use of Transactions in Database Operations**
   - **Consistent State Management:** Transactions are used to ensure that all database operations either complete fully or not at all. This is crucial in maintaining the consistency and integrity of the database.
   - **Atomic Operations:** By wrapping operations like table creation and data insertion within transactions, we ensure atomicity. This means that either all operations succeed, or in the event of an error, the database reverts to its previous state.
   - **Efficient Bulk Operations:** Transactions are particularly beneficial when inserting bulk data, as they allow for multiple operations to be treated as a single unit, enhancing performance and consistency.

#### 3. **Comprehensive Exception Handling in Database Interactions**
   - **Graceful Error Management:** Our code includes try-catch blocks to handle exceptions that may occur during database operations. This ensures that errors are caught and handled appropriately, preventing the application from crashing.
   - **Rollback on Error:** In case of an error, particularly within a transaction, changes are rolled back to maintain the database's integrity. This is evident in our approach to handling database-related errors and during data generation phases.
   - **Handling Various Error Types:** We have implemented error handling not just for database errors but for any other exceptions that might occur during script execution, providing a robust safety net for our operations.

#### 4. **Ensuring Data Integrity and Reliability**
   - **Reliable Database Setup and Maintenance:** From setting up the database schema to populating it with base and fake data, our approach ensures that each step is executed reliably, with error checks and rollbacks where necessary.
   - **Robust Query Execution:** The application's robustness is further demonstrated during query execution, where we handle potential issues gracefully, ensuring that the database operations are not only effective but also resilient to errors.

### Conclusion
The strategic use of transactions, comprehensive error handling, and enforcement of foreign key constraints in our health and fitness tracking app underscores our commitment to data integrity and operational reliability. This approach ensures that our database operations are not only efficient and consistent but also resilient to errors, providing a stable and reliable foundation for our application.


## Data Normalization in Health and Fitness Tracking App

Our health and fitness tracking app employs a comprehensive approach to data normalization, adhering to all five normal forms to ensure the database is optimized, consistent, and free from redundancy. Here's a detailed breakdown of how each normal form is applied:

### 1. **First Normal Form (1NF)**
- **Atomicity:** Each table column contains atomic values. For instance, in the `Users` table, columns like `FirstName`, `LastName`, `DateOfBirth`, and `Sex` store single, indivisible values.
- **Unique Primary Keys:** Every table has a unique primary key. For example, `UserID` in the `Users` table and `SleepID` in the `DailySleep` table.

### 2. **Second Normal Form (2NF)**
- **Eliminating Partial Dependency:** All non-key attributes are fully functionally dependent on the primary key. For example, in the `UserHealth` table, both `Height` and `Weight` are dependent on `UserID`, not on a subset of the primary key.
- **Separation of Data:** Data is separated based on primary key dependency. For instance, user authentication details are in the `Authentication` table, separate from the `Users` table, to avoid partial dependency.

### 3. **Third Normal Form (3NF)**
- **Eliminating Transitive Dependency:** Non-key attributes are not dependent on other non-key attributes. For example, in the `DailySleep` table, `SleepDuration` is calculated directly from `SleepStart` and `SleepEnd`, and does not depend on any other non-key attribute.
- **Separation of Non-Key Attributes:** Tables like `DailyActivity` separate attributes like `WaterIntake`, `TotalCaloriesBurned`, and `TotalCaloriesConsumed`, ensuring they are not dependent on each other but only on the primary key (`ActivityID`).

### 4. **Boyce-Codd Normal Form (BCNF)**
- **Refined 3NF:** Our database design refines 3NF by ensuring every determinant is a candidate key. For example, in the `Authentication` table, `Username` and `Email` are unique and not just functionally dependent on `UserID` but also candidate keys in their own right.
- **Strong Entity Relationships:** The relationships between entities, such as between `Users` and `Authentication`, are strong and well-defined, with foreign keys ensuring referential integrity.

### 5. **Fourth and Fifth Normal Forms (4NF and 5NF)**
- **Handling Multi-Valued Dependencies:** Our design avoids multi-valued dependencies. Each table represents a single theme or concept, such as `UserWorkouts` focusing solely on user workout sessions.
- **Avoiding Join Dependencies:** The database design ensures that no table is subject to a join dependency that is not a consequence of the candidate keys. This means tables can be reconstructed from their decomposed forms without loss of information.

### Conclusion
By adhering to these normalization principles, our database design ensures efficiency, consistency, and integrity of data. This approach minimizes redundancy, optimizes storage, and enhances the performance of our health and fitness tracking application. Each decision in the database structure, from the separation of user authentication details to the calculation of sleep duration, is made with these normalization rules in mind, ensuring a robust and reliable database system.

