# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 14:25:48 2023

@author: ashutosh jha
"""

def farenheitTOcelcius(s,i):
    s=str(s);
    s.lower();
    i=int(i);
    if s=="c":
        F=(i*9/5)+32
        return (F);
    else:
        C=(i-32)*5/9;
        return (C);
        
    
        
        
        
        
    