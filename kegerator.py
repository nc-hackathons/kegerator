#!/usr/bin/python
import os
import time
import math
import logging
from Flow_Meter import *
import RPi.GPIO as GPIO

KEG_PIN_1 = 4

GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(KEG_PIN_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)


fm = Flow_Meter(1)

# Beer, on Pin 4
def doAClick(channel):
  currentTime = int(time.time() * 1000)
  if fm.enabled == True:
    fm.update(currentTime)

def sendData(flow_meter):
  flow_meter.getFormattedThisPour()
  flow_meter.fm_id

"""
def doAClick2(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if fm2.enabled == True:
    fm2.update(currentTime)
"""

GPIO.add_event_detect(KEG_PIN_1, GPIO.RISING, callback=doAClick, bouncetime=20) # Beer, on Pin 23
#GPIO.add_event_detect(24, GPIO.RISING, callback=doAClick2, bouncetime=20) # Root Beer, on Pin 24

# main loop
while True:
  currentTime = int(time.time() * 1000)
  print fm.lastClick
  print fm.thisPour
  if (fm.thisPour > .01 and currentTime - fm.lastClick > 3000):
    print "Someone just poured " + fm.getFormattedThisPour() + " of beer from the keg"
    sendData(fm)
    fm.reset();
