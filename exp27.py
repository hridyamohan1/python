#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:25:38 2023

@author: sree
"""

n=int(input("Enter no.of words:"))
list=[]
for i in range(n):
    x=input("Enter word: ")
    list.append(x)
print(list)
max=len(list[0])
temp=list[0]
for i in list:
    if len(i)>max:
        max=len(i)
        temp=i
print("Longest word is ",temp," with length ",max)