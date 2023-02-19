#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:03:14 2023

@author: sree
"""

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
i=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        gcd=i
    i+=1
print("GCD:",gcd)
