import math

def calculateStats(numbers):
  # return computedStats here.
  # check numbers for math.isnan
  computedStats = {}
  if math.isnan(numbers):
    computedStats["min"] = float('nan')
    computedStats["max"] = float('nan')
    computedStats["avg"] = float('nan')
  else:
    computedStats["min"] = math.min(numbers)
    computedStats["max"] = math.max(numbers)
    computedStats["avg"] = math.sum(numbers)/math.len(numbers)
  return computedStats

class EmailAlert:
  
