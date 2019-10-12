# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:51:22 2019

@author: Huiying Chen
"""
# numberLists.py
# CS 453
# Written by Huiying Chen
# Date written 14 Sep 2019
# Date/time last modified 17 Sep 2019
# Purpose: Convert input to a list, manipulate, and print results
# Input: A list of integers enclosed in square brackets, with elements separated by commas. The integers may be positive, negative, or zero.
# Output: Associate information of this list

# Ask user to type an integer list
string = input('Please type an integer list, enclosed in square brackets, with elements separated by commas: ')

# 1)10)Get the list without square brackets, and remove spaces of elements in the list
stringCut = string[1:-1]
# 3)4)Case that the list is empty
if stringCut == '':
    print('This list is empty.')
else: 
    integer_list = stringCut.split(',')
# Print list before remove spaces 
    print('The list may contain spaces is: ', integer_list)
# Print list after remove spaces
    integer_list = [x.strip(' ') for x in integer_list]
    print('The list after remove spaces is: ', integer_list)

# Convert elements to integer and print elements in the list
    integer_list = list(map(int, integer_list))
    print('The list after convert elements to integers is: ', integer_list)
# 2)Print the length of the list
    print("The length of the list is: ", len(integer_list))

# 3)4)If the list is not empty, print the first and the last element of the list
    print('The first element of the list is: ', integer_list[0])
    print('The last element of the list is: ', integer_list[-1])

# 5)Print the sum of the numbers in the list
    sum_list = sum(integer_list)
    print('Sum of the list is: ', sum_list)

# 6)Create a new list that contains only the positive values from the input list
    positive_list = []
    for i in integer_list:
        if i > 0:
            positive_list.append(i)
    print('Positive values from the input list are: ', positive_list)

# 7)Find whether this list has a zero value
    if integer_list.count(0) != 0:
        print('The index of the first zero in the list is: ', integer_list.index(0))
    else:
        print('The list does not contain a zero.')

# 8)Print the list in reverse
    reverse_list = integer_list[::-1]
    print('The list in reverse is: ', reverse_list)

#9) Create a new list that contains the sorted elements of the input list
    sorted_list = []
    sorted_list = sorted(integer_list)
    print('The list after sorted is: ', sorted_list)

    












