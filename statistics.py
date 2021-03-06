def calculateStats(numbers):
	computedStats = {}
	computedStats["min"] = float('nan')
	computedStats["max"] = float('nan')
	computedStats["avg"] = float('nan')
	if numbers:
		computedStats["min"] = min(numbers)
		computedStats["max"] = max(numbers)
		computedStats["avg"] = sum(numbers)/len(numbers)
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
		calculatedstats = calculateStats(values)
		#print(calculatedstats)
		if calculatedstats["max"] > self.maxThreshold:
			self.alert[0].emailSent = True
			self.alert[1].ledGlows = True
