import math

def calculateStats(numbers):
  # return computedStats here.
  # check numbers for math.isnan
  computedStats = {}
  if numbers  == []:
    computedStats["min"] = float('nan')
    computedStats["max"] = float('nan')
    computedStats["avg"] = float('nan')
  else:
    computedStats["min"] = math.min(numbers)
    computedStats["max"] = math.max(numbers)
    computedStats["avg"] = math.sum(numbers)/math.len(numbers)
  return computedStats

class EmailAlert:
  def __init__(self):
    self.emailSent = False
        
class LEDAlert:
  def __init__(self):
    self.ledGlows = False
        
class StatsAlerter:
  def __init__(self, maxThreshold, alert):
    self.maxThreshold = maxThreshold
    self.alert = alert
  def checkAndAlert(self, values):
    print(values)
      
    
