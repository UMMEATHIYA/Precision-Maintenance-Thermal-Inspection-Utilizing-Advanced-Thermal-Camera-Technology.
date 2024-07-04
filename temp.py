import sqlite3
import random
import time
import datetime

# Connect to the database
conn = sqlite3.connect('temp.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE data
             (timestamp datetime, variable1 real, variable2 real)''')

# Set initial values
value1 = random.uniform(0, 10)
value2 = random.uniform(0, 10)

# Set the linear trend coefficients
slope1 = 0.1
slope2 = 0.2

# Generate data for 10 seconds
for i in range(10):
    # Generate timestamp
    timestamp = datetime.datetime.now() 

    # Calculate new values with linear trend
    value1 += slope1
    value2 += slope2

    # Insert data into the database
    c.execute("INSERT INTO data VALUES (?, ?, ?)", (timestamp, value1, value2))

    # Wait for 1 second
    time.sleep(1)

# Commit changes and close the connection
conn.commit()
conn.close()
