import time
class Flow_Meter():
  enabled = True
  start_pouring = True
  fm_id = 0
  clicks = 0
  lastClick = 0
  clickDelta = 0
  hertz = 0.0
  flow = 0 # in Liters per second
  thisPour = 0.0 # in MilliLiters

  def __init__(self, fm_id):
    self.fm_id = fm_id
    self.clicks = 0
    self.lastClick = int(time.time() * 1000)
    self.clickDelta = 0
    self.hertz = 0.0
    self.flow = 0.0
    self.thisPour = 0.0
    self.enabled = True

  def update(self, currentTime):
    self.clicks += 1
    # get the time delta
    self.clickDelta = float(max((currentTime - self.lastClick), 1))
    # calculate the instantaneous speed
    if (self.enabled == True and self.clickDelta < 1000.):
      self.hertz = 1000. / self.clickDelta
      self.flow = self.hertz / (60 * 7.5) # In Liters per second
      instPour = self.flow * self.clickDelta
      self.thisPour += instPour
    # Update the last click
    self.lastClick = currentTime

  def getFormattedClickDelta(self):
     return str(self.clickDelta) + ' ms'

  def getFormattedHertz(self):
     return str(self.hertz) + ' Hz'

  def getFormattedFlow(self):
     return str(self.flow) + ' L/s'

  def getFormattedThisPour(self):
     return str(self.thisPour) + ' mL'


  def reset(self):
    self.thisPour = 0;
    self.clicks = 0;
    self.start_pouring = True
