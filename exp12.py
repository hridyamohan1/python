#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:49:12 2023

@author: sree
"""

n=int(input("Enter number of color:"))
list=[]
for i in range(n):
    x=input("Enter color")
    list.append(x)
print(list)
print("First color is ",list[0])
print("Last color is ",list[-1])