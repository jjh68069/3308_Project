import csv
from flask import Flask, render_template
app = Flask(__name__)

"""@package docstring
StockAnalysis Algorithms"""

class StockAnalysis:
	"""StockAnalysis Class Documentation"""

	def __init__(self, filename):

		self.filename = filename

	def momentum(self):
		"""Momentum Method - we start with a 6 column csv file: date, close,volume, open, high, low 
		and find the moving average by adding the past 20 days of closing prices and dividing by 20.
		 If the current price is above the moving average, that is considered auspicious for the stock's prospects. """
		companyCSV = self.filename
		v = open(companyCSV)
		r = csv.reader(v)
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
		"""Printing Results Method - prints the pertinent results of findMA function
		in terms of the recommendation status for the company. """
		MAandPrice = self.momentum()
		print("The moving average is: ", MAandPrice[0], "Last Close was: ", MAandPrice[1])
		if MAandPrice[0] >= MAandPrice[1]:
			print("The price is below the 20 day moving average, we do not recommend this company.")
		else:
			print("The price is above the 20 day moving average, it is a viable purchase.")

if __name__ == "__main__": 

	instance = StockAnalysis("nflx.csv")
	instance.printResults()
	


