#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 13:14:49 2023

@author: sree
"""


class Time:
    def __init__(self,hour,minutes,seconds):
        self.__hour=hour
        self.__minutes=minutes
        self.__seconds=seconds
    def __add__(self,other):
        hour=self.__hour+other.__hour
        minutes=self.__minutes+other.__minutes
        seconds=self.__seconds+other.__seconds
        if seconds>60:
            minutes+=int(minutes/60)
            seconds=(seconds%60)
        if minutes>60:
            hour+=int(minutes/60)
            minutes=(minutes%60)
        time="{0} hour : {1} minutes : {2} seconds ".format(hour,minutes,seconds)
        return time
h1=int(input("Enter hour of first time:"))
m1=int(input("Enter minutes of first time:"))
s1=int(input("Enter seconds of first time:"))
h2=int(input("Enter hour of second time:"))
m2=int(input("Enter minutesr of second time:"))
s2=int(input("Enter seconds of second time:"))
t1=Time(h1,m1,s1)
t2=Time(h2,m2,s2)
print("After adding time:",t1+t2)