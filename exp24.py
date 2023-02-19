#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:18:02 2023

@author: sree
"""

n=int(input("Enter step number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()