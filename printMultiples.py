#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 19:37:47 2018

@author: thayssilva
"""

def RangeIntervals(first=1,last=100):
    for num in range (first,last+1):
        key= multiples(num)
        print (key)

def multiples(number):
    key =number
    if number%3==0:
        key= "Three"
        if number%5 ==0:
            key="ThreeFive"
    elif number%5==0:
        key = "Five"
    return (key)