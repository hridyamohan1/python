#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 21:53:15 2023

@author: sree
"""

str=input("Enter a word:")
if str.endswith("ing"):
    str=str+"ly"
else:
    str=str+"ing"
print("Modified string is:",str)