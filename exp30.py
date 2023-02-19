#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:43:11 2023

@author: sree
"""

a=int(input("enter side of square:"))
s_area=lambda a:a*a
print("Area of square:",s_area(a))
l=int(input("enter length of rectangle:"))
b=int(input("enter breadth of rectangle:"))
r_area=lambda l,b:l*b
print("Area of square:",r_area(l,b))
l=int(input("enter breadth of triangle:"))
h=int(input("enter height of triangle:"))
t_area=lambda l,h:0.5*b*h
print("Area of square:",t_area(l,h))