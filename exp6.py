#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 19:29:29 2023

@author: sree
"""

list1=[1,2,3,4]
list2=[2,3,4,5]
s1=0
s2=0
print(list1)
print(list2)
if len(list1)==len(list2):
    print("Lists have same length")
else:
    print("Lists have different length")
for i in range(len(list1)):
    s1=s1+list1[i]
print("sum of list1:",s1)
for i in range(len(list2)):
    s2=s2+list2[i]
print("sum of list2:",s2)
if s1==s2:
    print("Sum of lists are same")
else:
    print("Sum of lists are different")
print("common element in lists are:")
for i in list1:
    for j in list2:
        if i==j:
            print(i)
            