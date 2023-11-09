# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:02:23 2023

@author: ashutosh jha
"""

def emailaddress(email):
    email=str(email);
    email.lower();
    if "@" not in email:
        return ("invalid");
    if "@"!=email[-1]:
        return ("valid");
    