#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 21:28:44 2023

@author: sree
"""

l=int(input("Enter 4 digit number:"))
u=int(input("Enter 4 digit number:"))
a=[]
def even(n):
    while(n!=0):
        a=n%10
        if(a%2==0):
            n//=10
        else:
            return False
    return True
if l<u:
    for i in range(l,u+1):
        z=int(i**(.5))
        if((i**(.5)==z) and even(i)):
            a.append(i)
    print("Perfect Number list:",a)
else:
    print("Pls answer the question correctly")