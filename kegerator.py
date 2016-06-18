import RPi.GPIO as GPIO
from Flow_Meter import *
from Monitor import *

FLOW_METER_PIN = 4
FLOW_METER_ID = 1

meter1 = Flow_Meter(FLOW_METER_PIN, FLOW_METER_ID)
monitor1 = Monitor(meter1)
monitor1.run()
"""
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_METER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)


def hello_world(pin_number):
    print "flow detected - " + str(pin_number)


GPIO.add_event_detect(FLOW_METER_PIN, GPIO.RISING, callback=hello_world, bouncetime=20)
"""
