#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:59:33 2023

@author: sree
"""

import graphics.rectangle as r
import graphics.circle as c
import graphics.trdgraphics.cuboid as cb
import graphics.trdgraphics.sphere as sp
print("Rectangle")
print("Area:",r.area(2,3))
print("Perimeter:",r.perimeter(2,3))
print("Circle")
print("Area:",c.area(4))
print("Perimeter:",c.perimeter(4))
print("Cuboid")
print("Area:",cb.area(2,3,4))
print("Perimeter:",cb.perimeter(2,3,4))
print("Sphere")
print("Area:",sp.area(2))
print("Perimeter:",sp.perimeter(2))

