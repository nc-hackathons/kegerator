#!/usr/bin/python
import os
import time
import math
import logging
import json
import boto3
from Flow_Meter import *
import RPi.GPIO as GPIO
from models import *
from sqlalchemy import *

KEG_PIN_1 = 4

GPIO.setmode(GPIO.BCM) # use real GPIO numbering
GPIO.setup(KEG_PIN_1,GPIO.IN, pull_up_down=GPIO.PUD_UP)
#GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)

sqs = boto3.resource('sqs', region_name='us-east-1')
queue = sqs.get_queue_by_name(QueueName='keg-o-meter')

fm = Flow_Meter(1)

# Beer, on Pin 4
def doAClick(channel):
  currentTime = int(time.time() * 1000)
  if fm.enabled == True:
    if fm.clicks == 0:
	send_sqs_message("ON")
	print "Someone just started pouring!"
    fm.update(currentTime)

def send_sqs_message(subject, amount=None):
  message = {
	'subject': subject,
  }
  if amount is not None:
    message['beer'] = amount
  queue.send_message(MessageBody=json.dumps(message)) 


def sendData(flow_meter):
  amount_poured = flow_meter.thisPour
  keg_id = flow_meter.fm_id
  current_batch = Batch.query.filter_by(current=True, keg_id=keg_id).first()
  pour_activity = Pour(current_batch, amount_poured)
  db.session.add(pour_activity)
  db.session.commit() # Adds pour to database
  send_sqs_message("OFF", amount_poured)

"""
def doAClick2(channel):
  currentTime = int(time.time() * FlowMeter.MS_IN_A_SECOND)
  if fm2.enabled == True:
    fm2.update(currentTime)
"""

GPIO.add_event_detect(KEG_PIN_1, GPIO.RISING, callback=doAClick, bouncetime=20) # Beer, on Pin 23
#GPIO.add_event_detect(24, GPIO.RISING, callback=doAClick2, bouncetime=20) # Root Beer, on Pin 24

# main loop
print "Starting kegerator monitor"
while True:
  currentTime = int(time.time() * 1000)
  if (fm.thisPour > .01 and currentTime - fm.lastClick > 3000):
    print "Someone just poured " + fm.getFormattedThisPour() + " of beer from the keg"
    sendData(fm)
    fm.reset();
