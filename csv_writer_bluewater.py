import csv
import time


def write_csv(ph_sensor, oxygen_sensor, temp_sensor):
    row = []
    time_current = round(time.time(), 0)    # Unix epoch time
    row.append(time_current)
    row.append(ph_sensor)
    row.append(oxygen_sensor)
    row.append(temp_sensor)
    print("appended to list")

    with open("sensor_data.csv", 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)
