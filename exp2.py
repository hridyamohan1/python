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


list=[1,2,3,4]
print(list)
newlist=[x*x for x in list]
print("Squares:",newlist)


word=input("Enter a word:")
print(word)
vowel=[x for x in word if x in "aeiouAEIOU"]
print("vowels in ",word," is:",vowel)


word=input("Enter a word:")
ord=[ord(x) for x in word]
print("ordinal value of ",word," is:",ord)