import sqlite3
import random
import time
import datetime

# Connect to SQLite database
conn = sqlite3.connect('stimulation.db')
c = conn.cursor()

# Create table to store data
c.execute('''CREATE TABLE IF NOT EXISTS accelerometer
             (timestamp DATETIME, vibration_x REAL, vibration_y REAL, vibration_z REAL)''')

c.execute('''CREATE TABLE IF NOT EXISTS temperature
             (timestamp DATETIME, temp_celsius FLOAT, temp_fahrenheit FLOAT)''')

c.execute('''CREATE TABLE IF NOT EXISTS speed_current_temperature
             (timestamp DATETIME, speed FLOAT, current_amp FLOAT, TEMPERATURE_CELSIUS FLOAT, Power FLOAT)''')

# Generate and insert random data for 20 timestamps
########################### ACCELEROMETER DATA ###################################
for i in range(100):
    timestamp = datetime.datetime.now() 
    vibration_x = random.uniform(-12, 12)
    vibration_y = random.uniform(-12, 12)
    vibration_z = random.uniform(-12, 12)
    c.execute("INSERT INTO accelerometer VALUES (?, ?, ?, ?)", (timestamp, vibration_x, vibration_y, vibration_z))
    time.sleep(0.1)  # wait 1 second before generating next data

# Generate and insert random data for 10 timestamps
########################### TEMPERATURE DATA ###################################

temp_celsius = random.uniform(23, 40)
temp_fahrenheit = random.uniform(73, 104)

slope1 = 0.1
slope2 = 0.2

for i in range(100):
    # Generate timestamp
    timestamp = datetime.datetime.now() 

    # Calculate new values with linear trend
    temp_celsius += slope1
    temp_fahrenheit += slope2

    c.execute("INSERT INTO temperature VALUES (?, ?, ?)", (timestamp, temp_celsius , temp_fahrenheit))
    time.sleep(0.1)  # wait 1 second before generating next data


# Generate and insert random data for 10 timestamps
########################### Speed, Current, Power vs TEMPERATURE DATA ###################################

speed = random.uniform(855, 1500)
current_amp = random.uniform(2.7, 9.5)
TEMPERATURE_CELSIUS = random.uniform(21, 31)
Power = random.uniform(550, 2000)

slope1 = 0.1
slope2 = 0.2
slope3 = 0.3
slope4 = 0.4


for i in range(100):
    # Generate timestamp
    timestamp = datetime.datetime.now() 

    # Calculate new values with linear trend
    speed += slope1
    current_amp += slope2
    TEMPERATURE_CELSIUS += slope3
    Power += slope4

    c.execute("INSERT INTO speed_current_temperature VALUES (?, ?, ?, ?, ?)", (timestamp, speed, current_amp, TEMPERATURE_CELSIUS, Power))
    time.sleep(0.1)  # wait 1 second before generating next data


# Commit changes and close connection
conn.commit()
conn.close()
