#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:26:09 2023

@author: sree
"""

n=int(input("Enter number of words:"))
list=[]
count=0
for i in range(n):
    x=input("Enter name")
    list.append(x)
print(list)
for i in list:
    for j in i:
        for 'a' in j:
            count+=1
print("occurance of a is:",count)