#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:07:22 2023

@author: sree
"""

list=[1,2,-2,-3,5]
print(list)
newlist=[x for x in list if x>0]
print("Positive numbers are:",newlist)