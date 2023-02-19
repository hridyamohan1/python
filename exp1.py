#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 18:29:38 2023

@author: sree
"""

c=int(input("Enter current year:"))
f=int(input("Enter final year:"))
print("Leap years between ",c," and ",f," are :")
for x in range(c,f+1):
    if x%4==0 and x%100!=0 or x%400==0:
        print(x)