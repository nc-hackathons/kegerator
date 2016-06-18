import RPi.GPIO as GPIO
import time

    FLOW_METER_PIN = 0
    KEG_ID = 0
    count = 0
    current_flow = 0
    time_stamp_first = 0
    time_stamp_last = 0

    def __init__(self, flow_meter_pin, keg_id):
        self.FLOW_METER_PIN = flow_meter_pin
        self.KEG_ID = keg_id
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(FLOW_METER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(FLOW_METER_PIN, GPIO.RISING, callback=process_flow_signal, bouncetime=20)


    def process_flow_signal(flow_meter_pin):
        print str(flow_meter_pin) + "\n"
        self.count += 1
        time_stamp_last = time.time()*1000.0
