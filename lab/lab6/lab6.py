# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 19:14:22 2019

@author: Huiying Chen
"""









def remove_punc( s ):
    new_s = ''
    for c in s: 
        if c.isprintable():
            if c.isalnum() or c.isspace() or c.isspace():
                new_s = new_s + c        
    return new_s




def word_count( s ):
    word = s.split()
    count = len(word)
    return count
    
    

def add_unique( s, word_list ):
    words = s.split()
    for word in words:
        if word.lower() not in word_list:
            word_list.append(word.lower())







s = "Depending on who you ask, there are nine (or eight) planets in the solar system. We're on the 3rd planet from the sun. We're on the 3rd planet from the sun."

new_s = remove_punc( s )
print( new_s )
count = word_count( new_s )
print(count)
word_list = []
add_unique( new_s, word_list )
print( word_list)










