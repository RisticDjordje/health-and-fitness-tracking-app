# User Experience Pipeline

## Registration Process
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

## Setting Goals

The next step in the registration process is setting goals. Here, users define their fitness goals through the following parameters:

- **Weight Goal:** Options include gain (bulk), lose (cut), or maintain.
- **Weight Goal Amount:** Specified in kilograms.
- **Average Night Sleep:** Measured in hours.
- **Average Daily Water Intake:** Recommendations are provided based on sex and weight.

To better understand these goals we need to understand some key processes.

#### Explanation of key processes
Besides BMR, another way people burn calories is through excercise and the amount of calories burned depends on the type of excercise they do and the duration of the excercise. For example, running burns more calories than walking. 

On the other hand, calories are replenished through food. The amount of calories depends on the type of food (protein, fat, carbohydrates, etc.) eaten and the quanityt. For example, a burger has more calories than a salad. 

Knowing this gives us enough information to calculate **the net calories**.

```
net calories = calories taken in by food - calories burned by excercise - BMR calories burned.
``` 

Now, if the user wants to **lose weight / cut**, they have to be in a **caloric deficit**. The usual recommended caloric deficit is 400 calories. This is the value that the user should be aspiring to achieve. 

If the user wants to **gain weight / bulk**, they have to be in a **caloric surplus**. The usual recommended caloric surplus is 400 calories (this is the NetCalorieChange for this goal). This is the value that the user should be aspiring to achieve.

If the user wants to maintain weight, they have to be in a **caloric balance**. This means that the net calories should be around 0.

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
Based on the user’s goal and the NetCalorieChange of that goal and the users current net calorie

## Dashboard and Analytics
The dashboard displays key metrics like daily water and sleep intake, 7-day averages for both. It also shows calories consumed and burned, and the net calorie count, telling users how many calories they have remaining to lose or intake to reach their daily goal (caloric deficit, surplus, or balance).














foreign key constraints using PRAGMA foreign_keys = ON to ensure referential integrity.

We added try-catch blocks to handle database-related errors and any other errors that may occur during the execution of the script.

If an error occurs, the code rolls back the changes to the database to maintain data consistency.

Added transactions to every insertion operation and extra try catches

