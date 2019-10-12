# -*- coding: utf-8 -*-

# loops.py
# CS 453
# Written by Huiying Chen
# Date written 24 Sep 2019
# Date/time last modified 25 Sep 2019
# Purpose: loops exercise
# Input: numbers or strings as required
# Output: numbers, strings, tables, lists as required

import re


print("\nProblem 1 - output the lowercase letters: ")
# a for loop to print the lowercase letters 'a' through 'z', one character per line.
letter = 'a'
while letter <= 'z':
    print(letter)
    letter = chr(ord(letter) + 1)
print()




print("\nProblem 2 - triangle of asterisks: ")
#Input a number from the user.
num = int(input('Please enter a number: '))
# Nested for loops to display a triangle made of asterisks.The number the user types determines the number of lines in the triangle.
if num >= 1 and num <= 50: 
    i = 1
    while i <= num:
        j = 1
        while j <= num:
            if j < i:
                print(' ', end = ' ')
            else:
                print('*', end = ' ')
            j = j + 1
        print()
        i = i + 1
else:
    print('Invalid input')
    
print()



print('\nProblem 3 - prime test')
# determine whether a positve integer number from user which should be greater than 1 is prime or not
#Input an integer from user
num = int(input('Please enter a positive number greater than 1: '))
#a while loop to ensure that the user has entered a positive number greater than 1.
while num > 1:
    prime = True
    i = 2
    #nested while loop with an else block to determine whether the number is prime or not and print an appropriate message.
    while i in range(2, num):
        if num % i == 0:
            prime = False
            break
        i = i + 1  
    if prime == True:
        print('This number is a prime number ')
        break
    else:
        print('This number is not a prime number ')
        break
#Error if user enter a non-positive number
else: 
    print('Error. You should enter a positive number greater than 1')
print()

     
        

print('\nProblem 4 - Counting vowels: ')
#input a string from user
string = input('Pleast enter a string: ') 
#convert to lowercase
string = string.lower() 
# a for loop that counts how many of each vowel (a, e, i, o, u) are found in the string
count = [0,0,0,0,0]
for char in string:
    if char == "a":
        count[0] = count[0] + 1
    elif char == "e":
        count[1] = count[1] + 1
    elif char == "i":
        count[2] = count[2] + 1
    elif char == "o":
        count[3] = count[3] + 1
    elif char == "u":
        count[4] = count[4] + 1
#display the number of times each vowel was found with numbers right aligned   
print("Number of 'a' is:  %4d" %count[0])
print("Number of 'e' is:  %4d" %count[1])
print("Number of 'i' is:  %4d" %count[2])
print("Number of 'o' is:  %4d" %count[3])
print("Number of 'u' is:  %4d" %count[4])
print()



print('\nProblem 5 - simple substitution cipher(CS 453): ')
#input a number to shift forward
shift = int(input('Please enter an integer number to shift forward: '))
#while loop to ensure the number is between 1-25  
while shift >= 1 and shift <= 25: 
    #input a string from user
    plaintext = input('Please enter a string: ')
    ciphertext = ''
    #wrap every letter in the plaintext string replaced by the letter 4 characters       forward in the alphabet
    for c in plaintext:
        #character to ASCII
        c_num = ord(c)
        #is the letter lowercase 'a' to 'z'?
        if (c_num >= ord('a')) and (c_num <= ord('z')):
            #get the number from 0-26, and replace 4 characters forward
            c_num = c_num - ord('a') + shift
            #wrap the number every 26 numbers
            c_num = c_num % 26
            #get the ciphered letters
            c_num = c_num + ord('a')
            ciphertext += chr(c_num) 

        #is the letter lowercase 'A' to 'Z'?
        elif (c_num >= ord('A')) and (c_num <= ord('Z')):
            #get the number from 0-26, and replace 4 characters forward
            c_num = c_num - ord('A') + shift
            #wrap the number every 26 numbers
            c_num = c_num % 26
            #get the ciphered letters
            c_num = c_num + ord('A')
            ciphertext += chr(c_num) 
        #other characters are NOT replaced
        else:
            ciphertext += chr(c_num)
    #print cipher text
    print(ciphertext)
    break
#else error message to inform user enter a proper number
else:    
    print('The integer number must be from 1 to 25, inclusive')
print()



print('\nProblem 6 - table of squares: ')
#display a table of numbers and their squares from 1 to 80 by using two nested for loops
#print the header of the table
print("%4s %6s %4s %6s %4s %6s %4s %6s" %('Num', 'Square', 'Num', 'Square', 'Num', 'Square', 'Num', 'Square'))
#print a 20-row, 8-column table of numbers and their squares from 1 to 80  by using two nested for loops
#vertical
for line in range (1,21):
    #horizontal
    i = line
    for column in range (1, 5):
        print ("%4d %6d" %(i,i*i), end = ' ')
        i = i + 20
    print()
print()       


  
print('\nProblem 7 - inputting words and sorting them: ')
#sort list from user input    
# initalize before the loop
list = []
word = input("Enter a word (type 'quit' to stop): ") 
#a sentinel loop to input words from the user
# while NOT the termination condition
while word.lower() != 'quit':    
    #inner while loop to check each input is only one word
    while re.match(r'\A[\w-]+\Z', word):
        #add to the list
        list.append(word)
        break
    #if input is not only one word
    else:
        print('error. One word only')
    # reset value at end of loop
    word = input("Enter a word (type 'quit' to stop): ")  
# while meets the termination condition
#sort the list
list.sort()
#print the sorted list one word per line
print('Your sorted list is:')
for word in list:
    print(word)
print()

