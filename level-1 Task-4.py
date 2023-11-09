# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:19:19 2023

@author: ashutosh jha
"""

number1=int(input());
number2=int(input());
operator=input();
if operator=="*":
    print(number1*number2);
elif operator=="+":
    print(number1+number2);
else:
    if operator=="-":
        print(number1-number2);
    if operator=="%":
        print(number1%number2);
    if operator=="/":
        try:
            print(number1/number2);
        except ZeroDivisionError:
            print("undefined")
        