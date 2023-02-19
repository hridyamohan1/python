#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:32:02 2023

@author: sree
"""

n=int(input("Enter a number:"))
print("Factors of",n," are:")
for i in range(1,n+1):
    if(n%i==0):
        print(i)