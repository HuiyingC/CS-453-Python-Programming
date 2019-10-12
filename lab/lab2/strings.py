# -*- coding: utf-8 -*-
"""
Created on Sat Sep 7 2019

@author: Huiying Chen
"""

# strings.py
# CS 153 or CS 453
# Written by Huiying Chen
# Date written 9/7/2019
# Date/time last modified 9/7/2019
# Purpose: Get a string from users. Then print a selected or modified string 
# Input: A string from user
# Output: A selected, modified string or certain characters of string as required

#ask user to input a string
my_str = input('Please input a string: ')
#get every word of the string
word_list = my_str.split()

#print the length of the string
print('The length of the string is:  ', len(my_str))

#print the first word of the string
print('The first word of the string is: ',word_list[0])

#print the string in all uppercase
print('The string in all uppercase is: ' ,my_str.upper())

#print the string in all lowercase
print('The string in all lowercase is: ' ,my_str.lower())

#print the string with all of the 'n' characters changed to 'm'
print("After the string with all of the 'n' characters changed to 'm' is: ", my_str.replace('n','m'))

#print the location of the first 'a' in the string
print("The location of the first 'a' in the string is: ", my_str.find('a'))

#print the string with all of spaces removed
print('The string with all of spaces removed is: ',my_str.replace(' ',''))

#print the last character of the string
print('The last character of the string is: ', my_str[-1])

# If the string is longer than 8 characters, print the first 8 characters of the string. Otherwise, print the 
#entire string
if len(my_str) > 8:
    print('The string is longer than 8 characters, the first 8 characters of the string are: ', my_str[0:7])
else:
    print('The string is shorter than or equal to 8 characters, the entire string is: ', my_str)










