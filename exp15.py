#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:56:28 2023

@author: sree
"""

a=input("Enter first string:")
b=input("Enter second string:")
s1=b[0]+a[1:]
s2=a[0]+b[1:]
print("After swapping:",s1+" "+s2)