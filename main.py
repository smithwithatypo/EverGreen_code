import time
import states_bluewater as states
import logic_bluewater as logic
import sensors_bluewater as sensors
import csv_writer_bluewater as csv_writer


while True:
    # sensors
    ph_sensor = float(sensors.get_devices()[1])
    oxygen_sensor = float(sensors.get_devices()[0])
    temp_sensor = sensors.get_temp()

    # logic to assign state variables
    base, acid = logic.ph_logic(ph_sensor)
    airblower = logic.oxygen_logic(oxygen_sensor)
    heater, chiller = logic.temp_logic(temp_sensor)

    # GPIO control
    states.acid_outlet(acid)
    states.base_outlet(base)
    states.airblower_outlet(airblower)
    states.heater_outlet(heater)
    states.chiller_outlet(chiller)

    # csv writer
    csv_writer.write_csv(ph_sensor, oxygen_sensor, temp_sensor)

    # optional - check if sensors work
    print(ph_sensor, oxygen_sensor, temp_sensor)

    # polling delay in seconds
    time.sleep(1800)
