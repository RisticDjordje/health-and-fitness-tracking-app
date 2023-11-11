from faker import Faker
import random, sqlite3
from datetime import datetime, timedelta
from faker_food import FoodProvider

fake = Faker()
fake.add_provider(FoodProvider)

conn = sqlite3.connect("database.db")
cursor = conn.cursor()


# Users
def generate_users(n=10):
    return [
        {
            "UserID": i,
            "FirstName": fake.first_name(),
            "LastName": fake.last_name(),
            "DateOfBirth": fake.date_of_birth(minimum_age=18, maximum_age=60),
            "Sex": random.choice(["Male", "Female"]),
        }
        for i in range(1, n + 1)
    ]


# Authentication
def generate_authentication(users):
    return [
        {
            "UserID": user["UserID"],
            "Username": fake.user_name(),
            "HashedPassword": fake.sha256(),
            "Email": fake.email(),
        }
        for user in users
    ]


def generate_daily_activity_for_today(user_health, users):
    # for each user generate an entry for today
    data = []
    for user in users:
        calories_burned = random.randint(0, 1500)
        calories_consumed = random.randint(1500, 3500)
        net_calories = (
            calories_consumed - calories_burned - user_health[user["UserID"] - 1]["BMR"]
        )
        water_intake = random.uniform(1, 4)
        data.append(
            {
                "UserID": user["UserID"],
                "Date": datetime.now().date(),
                "TotalCaloriesBurned": calories_burned,
                "TotalCaloriesConsumed": calories_consumed,
                "NetCalories": net_calories,
                "WaterIntake": water_intake,
            }
        )
    return data


# UserHealth
def generate_user_health(users):
    user_health_data = []
    for user in users:
        height = random.uniform(150, 200)
        weight = random.uniform(50, 100)
        bmi = weight / ((height / 100) ** 2)
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * (2023 - user["DateOfBirth"].year)
            + (5 if user["Sex"] == "Male" else -161)
        )

        user_health_data.append(
            {
                "UserID": user["UserID"],
                "Height": height,
                "Weight": weight,
                "BMI": bmi,
                "BMR": bmr,
            }
        )
    return user_health_data


# SleepGoal
def generate_sleep_goal(users):
    return [
        {"UserID": user["UserID"], "SleepGoal": random.randint(6, 10)} for user in users
    ]


#  DailySleep
def generate_daily_sleep(users, records_per_user=5):
    data = []
    for user in users:
        for _ in range(records_per_user):
            # start in recent 2 weeks
            start = fake.date_time_between(start_date="-14d", end_date="now")
            end = start + fake.time_delta(end_datetime="+8h")
            data.append(
                {
                    "SleepID": len(data) + 1,
                    "UserID": user["UserID"],
                    "SleepStart": start,
                    "SleepEnd": end,
                    "SleepDuration": (end - start).seconds / 3600,
                }
            )
    return data


# WeeklySleepAverage
def generate_weekly_sleep_average(users, daily_sleep_data):
    weekly_averages = []

    for user in users:
        user_id = user["UserID"]
        user_daily_sleep = [
            record for record in daily_sleep_data if record["UserID"] == user_id
        ]

        # Calculate the date range for the last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=6)

        # Filter daily sleep records within the date range for this user
        user_weekly_sleep = [
            record
            for record in user_daily_sleep
            if start_date <= record["SleepStart"] <= end_date
        ]

        if user_weekly_sleep:
            # Calculate the average sleep duration for the user's last 7 days
            average_sleep_duration = sum(
                record["SleepDuration"] for record in user_weekly_sleep
            ) / len(user_weekly_sleep)
            weekly_averages.append(
                {"UserID": user_id, "AverageSleepDuration": average_sleep_duration}
            )

    return weekly_averages


# WaterIntakeGoal
def generate_water_intake_goal_data(users_data):
    return [
        {"UserID": user["UserID"], "WaterIntakeGoal": random.randint(2, 4)}
        for user in users_data
    ]


# DailyWaterIntake
def generate_daily_water_intake_data(users_data):
    # the user will have 3-5 records per day and each record will be 1-2 hours apart
    # the users will have 8-10 days of records that happened in the last 2 weeks
    data = []
    for user in users_data:
        for _ in range(random.randint(8, 10)):  # 8-10 days of records
            date = fake.date_time_between(start_date="-14d", end_date="now")
            for _ in range(random.randint(3, 5)):
                data.append(
                    {
                        "WaterIntakeID": len(data) + 1,
                        "UserID": user["UserID"],
                        "WaterIntakeAmount": random.uniform(0.5, 1.5),
                        "WaterIntakeDatetime": date,
                    }
                )
                date += fake.time_delta(end_datetime="+2h")
    return data


# WeeklySleepAverage
def generate_weekly_water_intake_average(users_data, daily_water_intake_data):
    weekly_averages = []

    for user in users_data:
        user_id = user["UserID"]
        user_daily_water_intake = [
            record for record in daily_water_intake_data if record["UserID"] == user_id
        ]

        # Calculate the date range for the last 7 days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=6)

        # Filter daily water intake records within the date range for this user
        user_weekly_water_intake = [
            record
            for record in user_daily_water_intake
            if start_date <= record["WaterIntakeDatetime"] <= end_date
        ]

        if user_weekly_water_intake:
            # Calculate the average water intake for the user's last 7 days
            average_water_intake = sum(
                record["WaterIntakeAmount"] for record in user_weekly_water_intake
            ) / len(user_weekly_water_intake)
            weekly_averages.append(
                {"UserID": user_id, "AverageWaterIntake": average_water_intake}
            )

    return weekly_averages


# DailyMeals
def generate_daily_meals_data(users_data):
    # Generate daily meal data for each user with 3 to 5 meal entries per day,
    # and for every day in the last 14 days
    data = []
    food_names = []
    for user in users_data:
        # Calculate the date range for the last 14 days
        end_date = datetime.now()
        for day_offset in range(14):
            date = end_date - timedelta(days=day_offset)

            # Generate 3 to 5 meal entries for each day
            for _ in range(random.randint(3, 5)):
                data.append(
                    {
                        "MealID": len(data) + 1,
                        "UserID": user["UserID"],
                        "MealDate": date,
                        # Use faker to generate meal name, calories, and description
                        "MealName": fake.dish(),
                        "Calories": random.randint(500, 1500),
                        "MealDescription": fake.dish_description(),
                    }
                )
    return data


# UserTrainingGoal
def generate_user_training_goal_data(training_goals, users_data):
    data = []
    for user in users_data:
        goal = random.choice(training_goals)
        data.append({"UserID": user["UserID"], "GoalID": goal[0]})
    return data


# UserWorkouts
def generate_user_workouts_data(exercise_categories, users_data):
    # each user can have between 0-2 workouts per day
    # the users will have 4-10 days of records that happened in the last 2 weeks

    data = []
    for user in users_data:
        for _ in range(random.randint(4, 10)):
            date = fake.date_time_between(start_date="-14d", end_date="now")
            for _ in range(random.randint(0, 1)):
                # Choose a random workout from exercise categories
                workout = random.choice(exercise_categories)

                # Calculate workout duration in hours (between 0.5 to 2 hours)
                duration_hours = random.uniform(0.5, 1.5)

                # Calculate calories burned using AvgCaloriesBurnedPerMinute
                avg_calories_burned = workout[2]
                calories_burned = avg_calories_burned * duration_hours * 60

                data.append(
                    {
                        "UserID": user["UserID"],
                        "WorkoutID": workout[0],
                        "StartTime": date,
                        "EndTime": date + timedelta(hours=duration_hours),
                        "Duration": duration_hours,
                        "CaloriesBurned": calories_burned,
                    }
                )
                date += timedelta(hours=duration_hours)
    return data


# delete all data from tables
cursor.execute("DELETE FROM Users")
cursor.execute("DELETE FROM Authentication")
cursor.execute("DELETE FROM UserHealth")
cursor.execute("DELETE FROM SleepGoal")
cursor.execute("DELETE FROM DailySleep")
cursor.execute("DELETE FROM WeeklySleepAverage")
cursor.execute("DELETE FROM WaterIntakeGoal")
cursor.execute("DELETE FROM DailyWaterIntake")
cursor.execute("DELETE FROM WeeklyWaterIntakeAverage")
cursor.execute("DELETE FROM DailyMeals")
cursor.execute("DELETE FROM UserTrainingGoal")
cursor.execute("DELETE FROM UserWorkouts")
cursor.execute("DELETE FROM DailyActivity")

# get exercise types from database.db file table ExerciseTypes
exercise_categories = []
cursor.execute("SELECT * FROM ExerciseTypes")
exercise_categories = cursor.fetchall()

# get the table TrainingGoal from database.db file
cursor.execute("SELECT * FROM TrainingGoal")
training_goals = cursor.fetchall()

# get the table WorkoutsTable from database.db file
cursor.execute("SELECT * FROM WorkoutsTable")
workouts_table = cursor.fetchall()

users = generate_users(10)
authentication = generate_authentication(users)
user_health = generate_user_health(users)
daily_activity_for_today = generate_daily_activity_for_today(user_health, users)
sleep_goal = generate_sleep_goal(users)
daily_sleep = generate_daily_sleep(users)
weekly_sleep_average = generate_weekly_sleep_average(users, daily_sleep)
water_intake_goal_data = generate_water_intake_goal_data(users)
daily_water_intake_data = generate_daily_water_intake_data(users)
weekly_water_intake_average = generate_weekly_water_intake_average(
    users, daily_water_intake_data
)
daily_meals_data = generate_daily_meals_data(users)
user_training_goal_data = generate_user_training_goal_data(training_goals, users)
user_workouts_data = generate_user_workouts_data(workouts_table, users)


# insert into tables
def insert_data(table_name, data):
    for record in data:
        columns = ", ".join(record.keys())
        placeholders = ", ".join("?" * len(record))
        sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(sql, tuple(record.values()))


insert_data("Users", users)
insert_data("Authentication", authentication)
insert_data("UserHealth", user_health)
insert_data("DailyActivity", daily_activity_for_today)
insert_data("SleepGoal", sleep_goal)
insert_data("DailySleep", daily_sleep)
insert_data("WeeklySleepAverage", weekly_sleep_average)
insert_data("WaterIntakeGoal", water_intake_goal_data)
insert_data("DailyWaterIntake", daily_water_intake_data)
insert_data("WeeklyWaterIntakeAverage", weekly_water_intake_average)
insert_data("DailyMeals", daily_meals_data)
insert_data("UserTrainingGoal", user_training_goal_data)
insert_data("UserWorkouts", user_workouts_data)

conn.commit()
conn.close()
