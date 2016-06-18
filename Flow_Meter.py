import RPi.GPIO as GPIO
import time


class Flow_Meter:
    FLOW_METER_PIN = 0
    FLOW_METER_ID = 0
    count = 0
    #current_flow = 0
    time_stamp_first = 0
    time_stamp_last = 0

    def __init__(self, flow_meter_pin, FLOW_METER_ID):
        self.FLOW_METER_PIN = flow_meter_pin
        self.FLOW_METER_ID = FLOW_METER_ID
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.FLOW_METER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.FLOW_METER_PIN, GPIO.RISING, callback=self.process_flow_signal, bouncetime=20)

    def process_flow_signal(self, flow_meter_pin):
        print str(flow_meter_pin) + "\n"
        self.count += 1
        if self.time_stamp_first == 0:
            self.time_stamp_first = time.time()*1000.0
        self.time_stamp_last = time.time()*1000.0

    def get_all_info(self):
        return self.time_stamp_first, self.time_stamp_last, self.count

    def reset(self):
        self.FLOW_METER_PIN = 0
        self.FLOW_METER_ID = 0
        self.count = 0
        self.current_flow = 0
        self.time_stamp_first = 0
        self.time_stamp_last = 0
