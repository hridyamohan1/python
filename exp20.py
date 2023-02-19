#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:08:19 2023

@author: sree
"""

n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("Factorial of ",n," is ",fact)