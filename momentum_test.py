#!/usr/bin/env python3

import unittest
import momentum

class MomentumTestCase(unittest.TestCase):

	def test_init(self):
		filename ="aapl.csv"
		p = momentum.StockAnalysis(filename)
		
	def test_findMA(self):
		filename = "aapl.csv"
		p = momentum.StockAnalysis(filename)

	def test_printResults(self):
		filename = "aapl.csv"
		p = momentum.StockAnalysis(filename)
		assertEqual
