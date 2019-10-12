# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 14:13:03 2019

@author: Huiying Chen
"""
# lab5.py
# CS 453
# Written by Huiying Chen
# Date written 8 Oct 2019
# Date/time last modified 9 Oct 2019
# Purpose: functions exercise



# print the parameter string on multiple lines, 5 characters per line
# parameter: string - a string 
# Output: print the string on multiple lines, 5 characters per line. The last line of output may not have 5 characters
def print5(string):
    index = 0 
    for c in string:
        print("%s" %c, end="")
        index = index + 1;
        if(index % 5 == 0):
            print()


# determine the type of triangle: scalene, isosceles or equilateral
# parameter: side1, side2, side3 - the lengths of the sides of a triangle
# Output: a string - the type of the triangle
def triangleType(side1, side2, side3):
    if side1==side2==side3:
        answer = "equilateral"
    elif side1==side2 or side1==side3 or side2==side3:
        answer = "isosceles" 
    else:
        answer = "scalene"
    return answer
    
    
# monitor water needs and pump schedules for a large water tank
# parameter: 1) tank capacity (gallons), 2) current level (a value that indicates current water level, as a percentage of the tank capacity. 3) usage rate (gallons per day).
# criteria:A pump that refills the tank must be switched on when the current level drops below 50 (half full).
# Output: an integer -  the number of days (int) that the tank can operate at the current usage rate before the pump must be turned on
def pumpSchedule(capacity, percentage, usage):
    #error case if current level is already below 50
    if percentage < 50:
        return 0
    #error case if usage needs turn on pump every day
    if usage > capacity * 0.5:
        return 0
    #calculate gallons left before pump must be turned on
    left = (percentage - 50) / 100 * capacity
    days = (int)(left / usage)
    return days
        


    
#main program for testing 


print("Testing Function #1: \n")
stringF1 = input("Type a string: ")
print5(stringF1)
print("\n")


print("Testing Function #2: \n")
print(triangleType(7, 8, 9))
print(triangleType(6, 12, 6))
print(triangleType(3, 3, 6))
print(triangleType(2, 2, 2))
print("\n")


print("Testing Function #3: \n")
print(pumpSchedule(100, 40, 20))
print(pumpSchedule(100, 100, 60))
print(pumpSchedule(100, 50, 6))
print(pumpSchedule(100, 100, 4))
print(pumpSchedule(100, 60, 4))
print(pumpSchedule(200, 80, 10))
print("\n")






















