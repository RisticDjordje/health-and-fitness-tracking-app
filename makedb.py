import sqlite3
import os

# Database file path
db_file = 'database.db'

# Check if the database file exists and delete it
if os.path.exists(db_file):
    os.remove(db_file)

# Connect to the database
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

print('Creating database...')
print("Connected to 'database.db' database.")

print('Creating tables...')
# Read and execute the schema SQL script
with open('schema.sql', 'r') as schema_file:
    schema_script = schema_file.read()
    cursor.executescript(schema_script)
print('Tables created.')

print('Creating base data...')
# Read and execute the base_data.sql SQL script
with open('base_data.sql', 'r') as base_data_file:
    base_data_script = base_data_file.read()
    cursor.executescript(base_data_script)
conn.commit()
print('Base data created.')

# Close the connection before generating fake data
conn.close()

# Now generate fake data
print('Creating fake data...')
# Read and execute the fakedata.py
with open('fakedata.py', 'r') as fakedata_file:
    fakedata_script = fakedata_file.read()
    exec(fakedata_script)
print('Fake data created.')
