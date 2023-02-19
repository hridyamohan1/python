#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:19:37 2023

@author: sree
"""

str=input("Enter a string:")
count=0
for x in range(len(str)):
    if(str[x]!=" "):
        count+=1
print("Number of characters is:",count)