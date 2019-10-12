# -*- coding: utf-8 -*-
"""
Created on 2019-08-31 14:50

@author: Huiying Chen
"""

# temperatureConversion.py
# CS 453
# Written by Huiying Chen
# Date written 8/31/2019
# Date/time last modified 8/31/2019
# Purpose: This program is to achieve Temperature Conversion Purpose: Fahrenheit to Celsius
# Input: The float number of Temperature in degrees Fahrenheit(°F) 
# Output: The float number of Temperature in degrees Celsius (°C), formatted with one digit to the #         right of the decimal


 #input The float number of Temperature in degrees Fahrenheit(°F) 
fahrenheit = float(input("Please input the number of Temperature in degrees Fahrenheit(°F): "))

#calculate the number of Temperature in degrees Celsius (°C)
celsius = (fahrenheit - 32) * 5/9 

#print the number of Temperature in degrees Celsius (°C)
print("The Temperature in degrees Fahrenheit(°F): \n", fahrenheit, "°F", 
      "\n Convert to the Temperature in degrees Celsius (°C) is: \n %.1f" %celsius, "°C"
      "\n (formatted with one digit to the right of the decimal point)")
