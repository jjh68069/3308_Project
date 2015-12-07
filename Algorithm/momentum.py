import csv
from flask import Flask, render_template
app = Flask(__name__)

"""@package docstring
Momentum Algorithm"""

class StockAnalysis:
	"""StockAnalysis Class Docking"""

	def __init__(self, filename):

		self.filename = filename

	def findMA(self):
		"""Moving Average Docking:  we start with a 6 column csv file: date, close,volume, open, high, low """
		companyCSV = self.filename
		v = open(companyCSV)
		r = csv.reader(v)
			#row0 = next(r)
			#row0.append("20 DMA")
			#print(row0) # check completed, the new column header is added
		exampledata = list(r)
		sumlast20 = 0
		v.close()
		for i in range(21):
			if i == 0: continue
			sumlast20 += float(exampledata[i][1])

		twentyDMA = sumlast20/20
		dataTuple = (twentyDMA, float(exampledata[1][1]))
		return dataTuple
					
	def printResults(self):
		"""Printing Results of Algorithm Docking"""
		MAthenPrice = self.findMA()
		print("The moving average is: ", MAthenPrice[0], "Last Close was: ", MAthenPrice[1])
		if MAthenPrice[0] >= MAthenPrice[1]:
			print("The price is below the 20 day moving average, we do not recommend this company.")
		else:
			print("The price is above the 20 day moving average, it is a viable purchase.")
'''
if __name__ == "__main__": 

	instance = StockAnalysis("nflx.csv")
	instance.printResults()
'''


