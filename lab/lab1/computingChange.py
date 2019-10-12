# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 06:31:12 2019

@author: Huiying Chen
"""
# computingChange.py
# CS 453
# Written by Huiying Chen
# Date written 8/31/2019
# Date/time last modified 8/31/2019
# Purpose: This program calculates the number of bills needed to give change.
# Input: amount of change to give in dollars
# Output: number of bills (twenties, tens, fives, and ones)

#input amount of change
amount_to_change = int(input("Please input an integer amount of change: "))

#initialize rest of change
rest_of_change = 0
#caculate the number of twenties dollar bill(s)  to give in change
num_twenties = amount_to_change // 20
rest_of_change = amount_to_change % 20

#caculate the number of tens dollar bill(s)  to give in change
num_tens = rest_of_change // 10
rest_of_change = rest_of_change % 10

#caculate the number of fives dollar bill(s)  to give in change
num_fives = rest_of_change // 5

#caculate the number of ones dollar bill(s) to give in change
num_ones = rest_of_change % 5

#print the numbers of bill(s) to give in change
print('Change for $ is: ', amount_to_change)
print(num_twenties, 'twenties dollar bill(s)')
print(num_tens, 'tens dollar bill(s)' )
print(num_fives, 'fives dollar bill(s)' )
print(num_ones, 'ones dollar bill(s)' )
