# Constants
PH_LOW = 4
PH_HIGH = 10
OXYGEN_MID = 10
TEMP_LOW = 20
TEMP_HIGH = 30


def ph_logic(reading):
    if (reading < PH_LOW):
        return 1, 0   # base, acid
    if (reading > PH_LOW and reading < PH_HIGH):
        return 0, 0
    else:
        return 0, 1


def oxygen_logic(reading):
    if (reading < OXYGEN_MID):
        return 1
    else:
        return 0


def temp_logic(reading):
    if (reading < TEMP_LOW):
        return 1, 0    # heater, chiller
    if (reading > TEMP_LOW and reading < TEMP_HIGH):
        return 0, 0
    else:
        return 0, 1
