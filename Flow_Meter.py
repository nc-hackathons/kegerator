import time
class Flow_Meter():
  PINTS_IN_A_LITER = 2.11338
  enabled = True
  clicks = 0
  lastClick = 0
  clickDelta = 0
  hertz = 0.0
  flow = 0 # in Liters per second
  thisPour = 0.0 # in Liters
  totalPour = 0.0 # in Liters

  def __init__(self):
    self.clicks = 0
    self.lastClick = int(time.time() * 1000)
    self.clickDelta = 0
    self.hertz = 0.0
    self.flow = 0.0
    self.thisPour = 0.0
    self.totalPour = 0.0
    self.enabled = True

  def update(self, currentTime):
    self.clicks += 1
    # get the time delta
    self.clickDelta = max((currentTime - self.lastClick), 1)
    # calculate the instantaneous speed
    if (self.enabled == True and self.clickDelta < 1000):
      self.hertz = 1000 / self.clickDelta
      self.flow = self.hertz / (60 * 7.5)  # In Liters per second
      instPour = self.flow * (self.clickDelta / 1000)
      self.thisPour += instPour
      self.totalPour += instPour
    # Update the last click
    self.lastClick = currentTime

  def getFormattedClickDelta(self):
     return str(self.clickDelta) + ' ms'

  def getFormattedHertz(self):
     return str(round(self.hertz,3)) + ' Hz'

  def getFormattedFlow(self):
     return str(round(self.flow,3)) + ' L/s'

  def getFormattedThisPour(self):
     return str(round(self.thisPour,3)) + ' L'

  def getFormattedTotalPour(self):
     return str(round(self.totalPour,3)) + ' L'

  def clear(self):
    self.thisPour = 0;
    self.totalPour = 0;
