# -*- coding: utf-8 -*-
# lab6.py
# CS 453
# Written by Huiying Chen
# Date written 11 Oct 2019
# Date/time last modified 15 Oct 2019
# Purpose: Strings and file operation practice
"""
Created on Fri Oct 11 19:14:22 2019

@author: Huiying Chen
"""



# remove punctuation symbols from a string
# parameter: s - a string 
# return: a new string that contains the original string with all punctuation symbols removed.
def remove_punc( s ):
    s_list = []
    for c in s: 
        # if c is not a punctuation symbol, append to list 
        if c.isprintable():
            if c.isalnum() or c.isspace():
                s_list.append(c)
    #return new string without punctuation symbols
    return ''.join(s_list)

# count and return the number of words in the string
# parameter: s - a string that contains one or more words, separated by spaces(there are no punctuation symbols in the string)
# return: an integer, the number of words in the string
def word_count( s ):
    # split string to list
    word = s.split()
    count = len(word)
    return count
    
    
# split the string into words, then append the lowercase version of the words to word_list if they aren't already in the list
# parameter: 1) a string that contains one or more words, separated by spaces(there are no punctuation symbols in the string) 2) a list of strings
# return: none
def add_unique( s, word_list ):
    words = s.split()
    for word in words:
        #check if the word in lowercase already in the list, if not, append it
        if word.lower() not in word_list:
            word_list.append(word.lower())



# test functions
def main():
    # Initialize a count for number of punctuation symbols in the file
    count_punc = 0
    # Initialize a count for the total number of words in the file
    count = 0
    # hold the list of unique words in the file
    word_list = []
    # Input the name of a file from the keyboard
    filename = input("Type file name: ")
    # Open the file for reading
    myFile = open(filename, "r")
    # Repeat for each line in the file
    for line in myFile:
        print(line)
        new_line = remove_punc( line )
        print(new_line)
        # Determine the number of punctuation symbols in the line and add to count
        # If there's a newline at the end of the line, discard it
        if line[-1] == chr(10):
            count_punc += len(line) - len(new_line) - 1
        else:
            count_punc += len(line) - len(new_line)
        # Determine the number of words in the line and add to count.
        count += word_count( new_line )
        # Add any new words from this line to the list of unique words.
        add_unique( new_line, word_list )
    # Finish read file    
    if not line:
        myFile.close()
    # Display the number of punctuation symbols in the file
    print("Number of punctuation symbols: ", count_punc)    
    # Display the total number of words in the file
    print("Total words: ", count)   
    # Display the number of unique words in the file
    print("Unique words: ", len(word_list))
    # Sort the list of unique words
    word_list.sort()
    # Display the sorted list of unique words in 3 columns
    print(word_list)
    if len(word_list) % 3 == 0:
        h = len(word_list) // 3
    else:
        h = len(word_list) // 3 + 1
    print("Total rows: ", h)
    for i in range(h):
        #print("i =", i, end="")
        print("%-15s %-15s" %(word_list[i], word_list[i+h]), end = " ")
        if (i + 2*h) < len(word_list):
            print("%-15s" %(word_list[i+2*h]))
        else:
            print("%-15s" %(" "))
    
     
#check whether the program is being run standalone
if __name__ == '__main__': 
    main()







