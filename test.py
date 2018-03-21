#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:42:37 2018

@author: thayssilva
"""

import unittest
from printMultiples import multiples,RangeIntervals
from codeValidation import Inwardcode,OutwardCode,ValidatePostcode



class TestUnit(unittest.TestCase):
 
    def setUp(self):
        pass
    #Test Multiples Print
    def test1_numbers_3_print_Three(self):
        self.assertEqual( multiples(9), "Three")
 
    def test2_numbers_3_print_Five(self):
        self.assertEqual( multiples(5), 'Five')
        
    def test3_numbers_3and5_print_ThreeFive(self):
        self.assertEqual( multiples(45), "ThreeFive")
 
    def test4_numbers_NOT3and5_print_number(self):
        self.assertEqual( multiples(13),13)
        
    #Test Postcode Inwardcode
    def test1_Inwardcode_accept(self):
        self.assertEqual( Inwardcode("1BT"), True)

    def test2_Inwardcode_refuse(self):
        self.assertEqual( Inwardcode("1OT"), False)
    
    def test3_Inwardcode_refuse(self):
        self.assertEqual( Inwardcode("13T"), False)
    
    #Test Postcode OutwardCode
    def test5_OutwardCode_accept_2Digits(self):
        self.assertEqual( OutwardCode("B1"), True)
        
    def test6_OutwardCode_refuse_2Digits(self):
        self.assertEqual( OutwardCode("1V"), False)

    def test7_OutwardCode_accept_A99(self):
        self.assertEqual( OutwardCode("B32"), True)
        
    def test8_OutwardCode_refuse_A99(self):
        self.assertEqual( OutwardCode("X99"), False)
    
    def test9_OutwardCode_accept_A9A(self):
        self.assertEqual( OutwardCode("B3C"), True)
        
    def test10_OutwardCode_refuse_A9A(self):
        self.assertEqual( OutwardCode("B3R"), False)

    def test11_OutwardCode_accept_AA99(self):
        self.assertEqual( OutwardCode("AL21"), True)
        
    def test12_OutwardCode_refuse_AA99(self):
        self.assertEqual( OutwardCode("AZ21"), False)

    def test13_OutwardCode_accept_AA9A(self):
        self.assertEqual( OutwardCode("AL2M"), True)
        
    def test14_OutwardCode_refuse_AA9A(self):
        self.assertEqual( OutwardCode("AL2C"), False)
        
    def test15_ValidatePostcode_accept(self):
        self.assertEqual( ValidatePostcode("CH65 9AS"), True)
    
    def test16_ValidatePostcode_accept(self):
        self.assertEqual( ValidatePostcode("B37 7JS"), True)
    
    def test17_ValidatePostcode_accept(self):
        self.assertEqual( ValidatePostcode("NE47 6LW"), True)
    
    def test18_ValidatePostcode_refuse(self):
        self.assertEqual( ValidatePostcode("XE47 6LW"), False)
    
    def test19_ValidatePostcode_refuse(self):
        self.assertEqual( ValidatePostcode("XE47 6LO"), False)
    
    def test20_ValidatePostcode_refuse_Formating(self):
        self.assertEqual(ValidatePostcode("XE476LO"), "Postcode invalid format")
    
    def test21_ValidatePostcode_refuse_Formating(self):
        self.assertEqual(ValidatePostcode("XE"), "Postcode invalid format")
    
    def test22_OutwardCode_refuse_Formating(self):
        self.assertEqual( ValidatePostcode("XE47 6L%"), "Postcode does not accept special character")
        
 
    
 
if __name__ == '__main__':
    unittest.main()