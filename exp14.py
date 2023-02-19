#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:54:04 2023

@author: sree
"""

col1=["red","green","blue"]
col2=["yellow","red","black"]
print(col1)
print(col2)
for i in range(len(col1)):
    if col1[i] not in col2:
        print(col1[i])
