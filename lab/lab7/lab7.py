# -*- coding: utf-8 -*-
# lab7.py
# CS 453 Lab Assignment # 7
# Written by Huiying Chen
# Date written 23 Oct 2019
# Date last modified 23 Oct 2019
# Purpose: List Practice
"""
Created on Wed Oct 23 00:52:55 2019

@author: Huiying Chen
"""
import math

# remove non-alphabetic characters (letters) from a string
# parameter: s - a string 
# return: a new string that contains only the alphabetic characters (letters) of s
def remove_non_alpha( s ) :
    new_s = ""
    for c in s:
        # if is alphabetic, add to the new string
        if c.isalpha():
            new_s += c
    return new_s

# remove non-numeric characters (letters) from a string
# parameter: s - a string 
# return: a new string that contains only the numeric characters (letters) of s that can form a valid int or float number(numeric value can have a leading '+' or '-' and a float can have a decimal point (but only one decimal point)).
def remove_non_numeric( s ) :
    new_s = ""
    s_list = s.split()
    for item in s_list:
        # add to the new string if the character is a valid int or float number(may start with '+' or '-' and may have only one decimal point)
        if item.isnumeric() or (item.startswith('+') or item.startswith('-') and item[1:].replace('.','', 1).isnumeric()) or (item.replace('.','', 1).isnumeric()):
            new_s += item 
    return new_s
 

# extract only numbers from a list of strings
# parameter: a_list - a list of strings
# return: a new list 
def list_only_numbers( a_list ) :  
    new_list = []
    for item in a_list:
        # 1) call remove_non_numeric
        new_item = remove_non_numeric(item)
        # a)if the return value is not the empty string, convert the string to either int or float, and append to the new list, b)otherwise discard it
        if new_item != '':
            if new_item.count('.') == 1:
                new_list.append(float(new_item))
            else:
                new_list.append(int(new_item))
            
    return new_list
    


# Create and return a new list that contains strings that have only the letters (non-alphabetic characters have been removed) from the elements of a_list
# parameter: a_list - a list of strings
# return: a new list 
def only_letters ( a_list ):
    # use list comprehension and call remove_non_alpha function to remove non-alphabetic characters
    new_list = [remove_non_alpha(i) for i in a_list]
    return new_list
    

# list statistics
# parameter: a_list - a list of numbers
# return: a new list   
def list_stats( a_list ) :
    # 1) Find the sum of the elements in a_list and store it in a variable named list_sum
    list_sum = sum(a_list)
    # 2) Find the mean (average) of the elements and store it in a variable named mean
    mean = list_sum / len(a_list)
    # 3) Use a list comprehension to create a new list that applies the expression (i - mean) ** 2 to each element i of a_list. Store the new list in a variable named squares
    squares = [(i - mean) ** 2 for i in a_list]
    # 4) Find the sum of the elements in squares and store it in a variable named sq_sum
    sq_sum = sum(squares)
    # 5) Calculate the standard deviation
    # std_dev = square root of (sq_sum / (N - 1)), where N is the number of elements in the original list
    std_dev = math.sqrt(sq_sum / (len(squares) - 1))
    # 6) Return a list that contains [ list_sum, mean, std_dev ]
    return [list_sum, mean, std_dev]



# main function
def main( ) :
      
    # 1)Open file1.txt for reading
    inputFile = open("file1.txt", "r")
    # 2)Open output1.txt for writing
    outputFile = open("output1.txt", "w+")
    # 3)Reads lines from the input file
    for line in inputFile:
        #if line[-1] != chr(10):
        # a)create list3A, split the string and convert each element to lowercase
        list3A = [item.lower() for item in line.split()] 
        # b) create list3B, a list that has all nonalpha characters removed from the elements of list3A
        list3B = [remove_non_alpha(item) for item in list3A] 
        # c) create list3C, a list that contains the length of each element in list3B
        list3C = [len(item) for item in list3B] 
        # d) find the average length of the elements in list3B
        avg_len = sum(list3C)/len(list3C)
        # e) Write output to the output file
        # original line from the input file
        outputFile.write("Original line: " + line)   
        # elements of list3A with one space between elements
        outputFile.write("Words: " + " ".join(list3A) + "\n")
        # elements of list3B with one space between elements
        outputFile.write("Only Letters: " + " ".join(list3B) + "\n")
        # average
        outputFile.write("Average word length: %f" %(avg_len) + "\n")
        # ---a blank line---
        outputFile.write("\n")
    # 4) When the loop is finished, close both files   
    if not line:
        inputFile.close()
        outputFile.close()  
        
    # 5) Open file2.txt for reading
    inputFile2 = open("file2.txt", "r")
    # 6)Open output2.txt for writing
    outputFile2 = open("output2.txt", "w+")
    # 7)Reads lines from the input file
    for line in inputFile2:
        # a) Create list7A by splitting the string
        list7A = line.split()
        # b) Create list7B by calling the list_only_numbers function using list7A
        list7B = list_only_numbers(list7A)
        # c) Call the list_stats function, pass it list7B, and store the return value in a variable called stats
        stats = list_stats(list7B)

        # d) Write output to the output file
        # original line from the input file
        outputFile2.write("Original line: " + line) 
        # elements of list7B with one space between elements
        list7B_str = [str(i) for i in list7B]
        outputFile2.write("Numeric Data: " + " ".join(list7B_str) + "\n")
        # sum of the elements of list7B
        outputFile2.write("Sum: %f" %(stats[0]) + "\n")
        # mean of the elements of list7B
        outputFile2.write("Mean: %f" %(stats[1]) + "\n")
        # standard deviation of the elements of list7B
        outputFile2.write("Std Dev: %f" %(stats[2]) + "\n")
        # ---a blank line---
        outputFile2.write("\n")
    # e) When the loop is finished, close both files
    if not line:
        inputFile2.close()
        outputFile2.close()  

#check whether the program is being run standalone
if __name__ == '__main__': 
    main()    
    
    
    
    
    
    
    