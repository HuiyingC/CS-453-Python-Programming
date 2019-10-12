# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 13:35:30 2019

@author: Huiying Chen
"""

# ringArea.py
# CS 453
# Written by Huiying Chen
# Date written 8/31/2019
# Date/time last modified 8/31/2019
# Purpose: This program calculates the area of a ring.
# Input:  two float numbers: the radius of the inner circle and the radius of the outer circle.
# Output: the area of the ring, formatted with two digits to the right of the decimal 
#         point.

#import math module
import math


#input the radius of the inner circle and the radius of the outer circle
radius_of_inner_circle = float(input("Please input the radius of the inner circle: "))
radius_of_outer_circle = float(input("Please input the radius of the outer circle: "))

#calculate the area of the inner circle
area_of_inner_circle = math.pi * math.pow(radius_of_inner_circle, 2)

#calculate the area of the outer circle
area_of_outer_circle = math.pi * math.pow(radius_of_outer_circle, 2)

#calculate the area of the ring
are_of_ring = area_of_outer_circle - area_of_inner_circle

#print the area of the ring, formatted with two digits to the right of the decimal 
# point
print("The area of the ring between two circles is: %.2f" %are_of_ring, 
      "\n (formatted with two digits to the right of the decimal point)")




