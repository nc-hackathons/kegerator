import time
class  Monitor:
    flow_meter = None;
    last_pulse_time_stamp = 0

    def __init__(self, flow_meter):
        self.flow_meter = flow_meter
        self.last_pulse_time_stamp = 0

    def set_last_pulse_time_stamp(self, time_stamp):
        self.last_pulse_time_stamp = time_stamp

    def get_info_and_reset_last_pulse_time_stamp(self):
        self.last_pulse_time_stamp = 0
        last_pulse_time_stamp = self.flow_meter.get_all_info()[1]
        return self.flow_meter.get_all_info()

    def run(self):
        while True:
            self.set_last_pulse_time_stamp(self.flow_meter.get_all_info()[1])
            curr_time = time.time()*1000.0
            if self.last_pulse_time_stamp is not 0 and curr_time - self.last_pulse_time_stamp >= 4000:
                print self.get_info_and_reset_last_pulse_time_stamp()
		flow_meter.restart()
