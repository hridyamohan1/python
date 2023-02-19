#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:14:05 2023

@author: sree
"""

class Bank:
    def __init__(self,accno,name,typee,bal):
        self.accno=accno
        self.name=name
        self.typee=typee
        self.bal=bal
    def deposit(self,amount):
        self.bal=self.bal+amount
        print("Deposited successfully")
        return self.bal
    def withdraw(self,amount):
        if amount>self.bal:
            print("Insufficient balance")
            return self.bal
        else:
            self.bal=self.bal-amount
            print("Deposited successfully")
            return self.bal
b=Bank(1001,"hridya","savings",5000)
damount=int(input("Enter amount to be deposited:"))
print("Available balance:",b.deposit(damount))
wamount=int(input("Enter amount to be withdrawn:"))
print("Available balance:",b.withdraw(wamount))
        