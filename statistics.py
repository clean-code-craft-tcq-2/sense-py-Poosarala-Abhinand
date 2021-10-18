import math
def calculateStats(numbers):
  #return computedStats here.
  # check numbers for math.isnan
  computedStats = {}
  computedStats["min"] = math.min(numbers)
  computedStats["max"] = math.max(numbers)
  computedStats["avg"] = math.sum(numbers)/math.len(numbers)
  return computedStats


