#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 23:29:00 2023

@author: sree
"""

dic={'hridya':10,"asma":2,"rasna":4}
l=list(dic.items())
l.sort()
d=dict(l)
print("Ascending order:",d)
l=list(dic.items())
l.sort(reverse=True)
d=dict(l)
print("Descending order:",d)