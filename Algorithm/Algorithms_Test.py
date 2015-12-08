#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#J-Dog
#Come at me
"""Python Unit Testing for StockAnalysis Class"""

import unittest
import Algorithms

class StockAnalysisTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        """test_init assures that the filename passed in a parameter is the same filename being examined"""
        filename = "nflx.csv"
        p = Algorithms.StockAnalysis(filename)
        self.assertEqual(p.filename, filename, "'text' does not match input")

    # Add Your Test Cases Here...
    def testMomentum(self):
        """testMomentum ensures that the return type of findMA function is a tuple"""
        filename = "nflx.csv"
        p = Algorithms.StockAnalysis(filename)
        self.assertIsInstance(p.momentum(),tuple, "Error in return type")

    def testPrintResults(self):
        """testPrintResults ensures that the printResults function does not have a return value"""
        filename = "nflx.csv"
        p = Algorithms.StockAnalysis(filename)
        self.assertIsNone(p.printResults(), "Error in return type")



    
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

