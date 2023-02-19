#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:10:24 2023

@author: sree
"""

first=0
second=1
count=0
limit=int(input("Enter limit:"))
print("Fibonacci series upto ",limit," are:")
while count<limit:
    print(first)
    third=first+second
    first=second
    second=third
    count+=1
