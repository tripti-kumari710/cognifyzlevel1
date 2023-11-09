# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 20:05:58 2023

@author: ashutosh jha
"""

def palindrome(word):
    reverse=word[::-1];
    if word==reverse:
        return True;
    else:
        return False;
        
    