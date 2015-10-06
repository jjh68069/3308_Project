import csv


def main():
	#ticker = input("which stock would you like an opinion of?")
	#will make call to api with this ticker in the future
	lastTwenty = []
	#we start with a 6 column csv file: date, close,volume, open, high, low
	filename = "aapl.csv"
	v = open(filename)
	r = csv.reader(v)
	row0 = next(r)
	row0.append("20 DMA")
	print(row0) # check completed, the new column header is added
	exampledata = list(r)
	sumlast20 = 0
	for i in range(21):
		if i == 0: continue
		sumlast20 += float(exampledata[i][1])
	print("The moving average is: ", sumlast20/20, "Last Close was: ", exampledata[1][1])
	if sumlast20/20 >= float(exampledata[1][1]):
		print("The price is below the 20 day moving average, we do not reccommend this company.")
	else:
		print("The price is above the 20 day moving average, it is a viable purchase.")
'''
	sumLast20 = 0
	for i in next(r) in range(0,20):
		#sumLast20 += item[1]
		print(item[i])
	#for item in r:
'''




if __name__ == "__main__": main()