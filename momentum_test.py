#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#J-Dog
#Come at me

import unittest
import momentum

class MomentumTestCase(unittest.TestCase):

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
        filename = "nflx.csv"
        p = momentum.StockAnalysis(filename)
        self.assertEqual(p.filename, filename, "'text' does not match input")

    # Add Your Test Cases Here...
    def testFindMA(self):
        filename = "nflx.csv"
        p = momentum.StockAnalysis(filename)
        self.assertIsInstance(p.findMA(),tuple, "Error in return type")

    def testPrintResults(self):
        filename = "nflx.csv"
        p = momentum.StockAnalysis(filename)
        self.assertIsNone(p.printResults(), "Error in return type")



    
# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()

