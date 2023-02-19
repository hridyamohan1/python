#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:06:56 2023

@author: sree
"""

class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
l1=int(input("Enter length of rectangle1:"))
b1=int(input("Enter breadth of rectangle1:"))
r1=Rectangle(l1,b1)
print("Area of rectangle1 is:",r1.area())
l2=int(input("Enter length of rectangle2:"))
b2=int(input("Enter breadth of rectangle2:"))
r2=Rectangle(l2,b2)
print("Area of rectangle1 is:",r2.area())
a1=r1.area()
a2=r2.area()
if a1<a2:
    print("Area of rectangle1 is small")
else:
    print("Area of rectangle2 is small")