#!usr/bin/env python3

#this file can be run to update the information in the database
#it will get the most recent from quandl.
#refer to this article for how to access data in the database: https://docs.python.org/2/library/sqlite3.html

import sqlite3
import urllib.request
#import urllib2
import os #gets file path location
import csv

conn = sqlite3.connect('stocks.db')

stock_ticker = ["MMM", "ABT", "ABBV", "ACN", "ACE", "ADBE", "ADT", "AES", "AET", "AMG", "AFL", "A", "GAS", "APD", "ARG", "AKAM", "AA", "ALXN", "ATI", "ALLE", "AGN", "ADS", "ALL", "ALTR", "MO", "AMZN", "AEE", "AAL", "AEP", "AXP", "AIG", "AMT", "AMP", "ABC", "AME", "AMGN", "APH", "APC", "ADI", "ANTM", "AON", "APA", "AIV", "AAPL", "AMAT", "ADM", "AIZ", "T", "ADSK", "ADP", "AN", "AZO", "AVGO", "AVB", "AVY", "BHI", "BLL", "BAC", "BK", "BCR", "BAX", "BBT", "BDX", "BBBY", "BRK-B", "BBY", "BIIB", "BLK", "BA", "BWA", "BXP", "BSX", "BMY", "BRCM", "BF-B", "CHRW", "CA", "CVC", "COG", "CAM", "CPB", "COF", "CAH", "KMX", "CCL", "CAT", "CBG", "CBS", "CELG", "CNP", "CTL", "CERN", "CF", "CHK", "CVX", "CMG", "CB", "CI", "XEC", "CINF", "CTAS", "CSCO", "C", "CTXS", "CLX", "CME", "CMS", "COH", "KO", "CCE", "CTSH", "CL", "CMCSA", "CMA", "CSC", "CAG", "COP", "CNX", "ED", "STZ", "GLW", "COST", "CCI", "CSX", "CMI", "CVS", "DHI", "DHR", "DRI", "DVA", "DE", "DLPH", "DAL", "XRAY", "DVN", "DO", "DTV", "DFS", "DISCA", "DG", "DLTR", "D", "DOV", "DOW", "DPS", "DTE", "DD", "DUK", "DNB", "ETFC", "EMN", "ETN", "EBAY", "ECL", "EIX", "EW", "EA", "EMC", "EMR", "ENDP", "ESV", "ETR", "EOG", "EQT", "EFX", "EQIX", "EQR", "ESS", "EL", "ES", "EXC", "EXPE", "EXPD", "ESRX", "XOM", "FFIV", "FB", "FDO", "FAST", "FDX", "FIS", "FITB", "FSLR", "FE", "FISV", "FLIR", "FLS", "FLR", "FMC", "FTI", "F", "FOSL", "BEN", "FCX", "FTR", "GME", "GPS", "GRMN", "GM", "GD", "GE", "GGP", "GIS", "GPC", "GNW", "GILD", "GS", "GT", "GOOGL", "GWW", "HRB", "HAL", "HBI", "HOG", "HAR", "HRS", "HIG", "HAS", "HCA", "HCP", "HCN", "HP", "HSY", "HES", "HPQ", "HD", "HON", "HRL", "HSP", "HST", "HCBK", "HUM", "HBAN", "ITW", "IR", "INTC", "ICE", "IBM", "IFF", "IP", "IPG", "INTU", "ISRG", "IVZ", "IRM", "JEC", "JNJ", "JCI", "JOY", "JPM", "JNPR", "KSU", "K", "GMCR", "KEY", "KMB", "KIM", "KMI", "KLAC", "KSS", "KRFT", "KR", "LB", "LLL", "LH", "LRCX", "LM", "LEG", "LEN", "LUK", "LVLT", "LLY", "LNC", "LLTC", "LMT", "L", "LOW", "LYB", "MTB", "MAC", "M", "MNK", "MRO", "MPC", "MAR", "MMC", "MLM", "MAS", "MA", "MAT", "MKC", "MCD", "MHFI", "MCK", "MJN", "MDT", "MRK", "MET", "KORS", "MCHP", "MU", "MSFT", "MHK", "TAP", "MDLZ", "MON", "MNST", "MCO", "MS", "MOS", "MSI", "MUR", "MYL", "NDAQ", "NOV", "NAVI", "NTAP", "NFLX", "NWL", "NFX", "NEM", "NWSA", "NEE", "NKE", "NI", "NE", "NBL", "JWN", "NSC", "NTRS", "NOC", "NRG", "NUE", "NVDA", "ORLY", "OXY", "OMC", "OKE", "ORCL", "OI", "PCAR", "PH", "PDCO", "PAYX", "PNR", "PBCT", "POM", "PEP", "PKI", "PRGO", "PFE", "PCG", "PM", "PSX", "PNW", "PXD", "PBI", "PCL", "PNC", "PPG", "PPL", "PX", "PCP", "PCLN", "PFG", "PG", "PGR", "PLD", "PRU", "PSA", "PEG", "PHM", "PVH", "QEP", "QRVO", "QCOM", "PWR", "DGX", "RL", "RRC", "RTN", "O", "RHT", "REGN", "RF", "RSG", "RAI", "RHI", "ROK", "COL", "ROP", "ROST", "RCL", "R", "SNDK", "SCG", "HSIC", "SLB", "SCHW", "SNI", "STX", "SEE", "SRE", "SHW", "SIAL", "SPG", "SWKS", "SLG", "SJM", "SNA", "SO", "LUV", "SWN", "SE", "STJ", "SWK", "SPLS", "SBUX", "HOT", "STT", "SRCL", "SYK", "STI", "SYMC", "SYY", "TROW", "TGT", "TEL", "TE", "TGNA", "THC", "TDC", "TSO", "TXN", "TXT", "TMO", "TIF", "TWX", "TWC", "TJX", "TMK", "TSS", "TSCO", "RIG", "TRV", "TRIP", "FOXA", "TYC", "TSN", "USB", "UA", "UNP", "UPS", "URI", "UTX", "UNH", "UHS", "UNM", "URBN", "VLO", "VAR", "VTR", "VRSN", "VZ", "VRTX", "VFC", "VIAB", "V", "VNO", "VMC", "WMT", "WBA", "DIS", "WM", "WAT", "WEC", "WFC", "WDC", "WU", "WY", "WHR", "WFM", "WMB", "WYN", "WYNN", "XEL", "XRX", "XLNX", "XL", "XYL", "YHOO", "YUM", "ZBH", "ZTS"]


#deciding where to store the csv data
#got code from here: http://stackoverflow.com/questions/1270951/python-how-to-refer-to-relative-paths-of-resources-when-working-with-code-repo
working_directory = os.getcwd()
file_path = os.path.join(working_directory + '/data')

for i in stock_ticker[0:1]:
	print (i)
	#please note that this is soham's api key
	url = 'https://www.quandl.com/api/v3/datasets/WIKI/{0}/data.csv?api_key= eFWztrj8CjJUa4zjQ2Mz'.format(i)
	print (url)
	response = urllib.request.urlopen(url)