import sqlite3
import os

# Database file path
db_file = 'database.db'

try:
    # Check if the database file exists and delete it
    if os.path.exists(db_file):
        os.remove(db_file)

    # Connect to the database and enable foreign key constraints
    conn = sqlite3.connect(db_file)
    conn.execute('PRAGMA foreign_keys = ON')
    cursor = conn.cursor()

    print('\nCreating database...')
    print(f"Connected to '{db_file}' database.")

    print('\nCreating tables...')
    # Read and execute the schema SQL script
    with open('schema.sql', 'r') as schema_file:
        schema_script = schema_file.read()
        cursor.executescript(schema_script)
    print('Tables created.')

    print('\nCreating base data...')
    # Read and execute the base_data.sql SQL script
    with open('base_data.sql', 'r') as base_data_file:
        base_data_script = base_data_file.read()
        cursor.executescript(base_data_script)
    conn.commit()
    print('Base data created.')

except sqlite3.Error as e:
    # Handle database-related errors
    print(f"Database error: {e}")
    if conn:
        conn.rollback()  # Rollback changes if an error occurs
finally:
    if conn:
        conn.close()

try:
    # Now generate fake data
    print('Creating fake data...')
    # Read and execute the fakedata.py
    with open('fakedata.py', 'r') as fakedata_file:
        fakedata_script = fakedata_file.read()
        exec(fakedata_script)
    print('Fake data created.')

except Exception as e:
    # Handle any other errors that may occur during fake data generation
    print(f"Error during fake data generation: {e}")

try:
    # Open the database again for running queries
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print("\nRunning queries...")
    # queries are located in the queries folder
    queries = os.listdir('queries')
    for query in queries:
        with open(f'queries/{query}', 'r') as query_file:
            query_script = query_file.read()
            print(f"\nRunning query: {query}")
            cursor.execute(query_script)
            results = cursor.fetchall()
            for result in results:
                print(result)

except sqlite3.Error as e:
    # Handle database-related errors during query execution
    print(f"Database error during query execution: {e}")
except Exception as e:
    # Handle other errors during query execution
    print(f"Error during query execution: {e}")
finally:
    if conn:
        conn.close()
