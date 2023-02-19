#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:29:34 2023

@author: sree
"""

n=int(input("Enter step number:"))
for i in range(n):
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
