# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:52:42 2019

@author: Huiying Chen
"""

# incomeTax.py
# CS 153 or CS 453
# Written by Huiying Chen
# Date written 9/7/2019
# Date/time last modified 9/7/2019
# Purpose: Calculate tax owed based on the tier in which the user's annual salary fits
# Input:  An integer value for the annual salary
# Output: The amount of tax owed based on the tier in which input annual salary fits

#Input an integer value for the annual salary
annual_salary = int(input('Please type an integer value for the annual salary: '))
#Caculate the amount of tax owed. Round it to the nearest integer
#Check to make sure that the salary is greater than or equal to zero
if annual_salary >= 0:
    #Print the annual salary
    print('{:20s}{:^5}{:>10,d}'.format('Annual Salary:     ','$',annual_salary))
    #Determine the tax rate based on the tier in which the user's annual salary fits, and print related information
    if annual_salary <= 20000:
        tax_owned = round(annual_salary * 0.1)
        print('{:20s}{:^5}{:>10}'.format('Tax Rate: ',' ','10%'))
        print('{:20s}{:^5}{:>10,d}'.format('Tax Owned:  ','$',tax_owned))
    elif (annual_salary > 20000) and (annual_salary <= 50000):
        tax_owned = round(annual_salary * 0.15)
        print('{:20s}{:^5}{:>10}'.format('Tax Rate: ',' ','15%'))
        print('{:20s}{:^5}{:>10,d}'.format('Tax Owned:  ','$',tax_owned))
    elif (annual_salary > 50000) and (annual_salary <= 100000):
        tax_owned = round(annual_salary * 0.2)
        print('{:20s}{:^5}{:>10}'.format('Tax Rate: ',' ','20%'))
        print('{:20s}{:^5}{:>10,d}'.format('Tax Owned:  ','$',tax_owned))
    elif annual_salary > 100000:
        tax_owned = round(annual_salary * 0.25)
        print('{:20s}{:^5}{:>10}'.format('Tax Rate: ',' ','25%'))
        print('{:20s}{:^5}{:>10,d}'.format('Tax Owned:  ','$',tax_owned))
#If the input salary is inappropriate, skip all calculations and print an error message that reminds user to type proper salary
else:
    print('Error. Please type a positive integer amount of annual salary.')









