#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:36:34 2023

@author: sree
"""

a=input("Enter a string:")
print(a)
b=a[0]
s=a[1:len(a)]
for i in range(len(s)):
    if s[i]==a[0]:
        b=b+"$"
    else:
        b=b+s[i]
print("string is:",b)