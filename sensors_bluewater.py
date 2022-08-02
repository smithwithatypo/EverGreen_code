import time
import re
from w1thermsensor import W1ThermSensor
from AtlasI2C import AtlasI2C


def get_temp():
    water_temp_sensor = W1ThermSensor()
    water_temp_in_celsius = water_temp_sensor.get_temperature()
    return water_temp_in_celsius


# gets DO, pH from I2C bus
def get_devices():
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []

    for i in device_address_list:
        device.set_i2c_address(i)
        device.write("R")
        time.sleep(2)    # default is 2
        raw_output = device.read()
        temp_output = raw_output.split(':')[1]
        clean_output = re.search(r"[.\d]+", temp_output).group()
        device_list.append(clean_output)
    return device_list
