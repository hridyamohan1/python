#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:25:36 2023

@author: sree
"""

class Publisher:
    def __init__(self,publisher):
        self.publisher=publisher
    def display(self):
        print("Publisher:",self.publisher)
class Book(Publisher):
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display(self):
        super().display()
        print("Title:",self.title)
        print("Author",self.author)
class Python(Book):
    def __init__(self,publisher,title,author,price,npages):
        self.price=price
        self.npages=npages
        Book.__init__(self,title,author)
        Publisher.__init__(self,publisher)
    def display(self):
        super().display()
        print("Price:",self.price)
        print("Number of pages",self.npages)
b1=Python("ABC","Python Programming","John",600,250)
b1.display()
    
    