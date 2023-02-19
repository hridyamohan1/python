#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:42:11 2023

@author: sree
"""

print("Enter 3 numbers")
a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    print(a," is largest")
elif b>a and b>c:
    print(b," is largest")
else:
    print(c," is largest")