import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# assign GPIO pins
ACID_PIN = 16
BASE_PIN = 20
AIRBLOWER_PIN = 21
HEATER_PIN = 22
CHILLER_PIN = 23

# setup pins
GPIO.setup(ACID_PIN, GPIO.OUT)
GPIO.setup(BASE_PIN, GPIO.OUT)
GPIO.setup(AIRBLOWER_PIN, GPIO.OUT)
GPIO.setup(HEATER_PIN, GPIO.OUT)
GPIO.setup(CHILLER_PIN, GPIO.OUT)


# Output
def acid_outlet(state):
    if state == 0:
        GPIO.output(ACID_PIN, GPIO.LOW)
    if state == 1:
        GPIO.output(ACID_PIN, GPIO.HIGH)


def base_outlet(state):
    if state == 0:
        GPIO.output(BASE_PIN, GPIO.LOW)
    if state == 1:
        GPIO.output(BASE_PIN, GPIO.HIGH)


def airblower_outlet(state):
    if state == 0:
        GPIO.output(AIRBLOWER_PIN, GPIO.LOW)
    if state == 1:
        GPIO.output(AIRBLOWER_PIN, GPIO.HIGH)


def heater_outlet(state):
    if state == 0:
        GPIO.output(HEATER_PIN, GPIO.LOW)
    if state == 1:
        GPIO.output(HEATER_PIN, GPIO.HIGH)


def chiller_outlet(state):
    if state == 0:
        GPIO.output(CHILLER_PIN, GPIO.LOW)
    if state == 1:
        GPIO.output(CHILLER_PIN, GPIO.HIGH)
