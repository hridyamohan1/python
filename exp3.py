#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:19:21 2023

@author: sree
"""

str=input("Enter a line of text:")
count=dict()
words=str.split()
for x in words:
    if x in count:
        count[x]+=1
    else:
        count[x]=1
print("Occurance of each word is:",count)