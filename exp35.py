#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:20:43 2023

@author: sree
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.__length=length
        self.__breadth=breadth
    def area(self):
        return self.__length*self.__breadth
    def __le__(self,other):
        return self.area() < other.area()
l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter breadth of rectangle1:"))
r1=Rectangle(l1,b1)
print("Area of rectangle1 is:",r1.area())
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter breadth of rectangle2:"))
r2=Rectangle(l2,b2)
print("Area of rectangle1 is:",r2.area())
if r1.area()<r2.area():
    print("Area of rectangle1 is small")
else:
    print("Area of rectangle2 is small")