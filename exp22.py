#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:13:28 2023

@author: sree
"""

n=int(input("Enter how many numbers:"))
list=[]
sum=0
for i in range(n):
    x=input("Enter number")
    list.append(x)
print(list)
for a in list:
    sum=sum+i
print("Sum:",sum)