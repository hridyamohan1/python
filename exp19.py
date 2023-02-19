#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:05:45 2023

@author: sree
"""

list=[1,2,3,4,5,6]
print(list)
for i in list:
    if i%2==0:
        list.remove(i)
print("list after removing even numbers:",list)