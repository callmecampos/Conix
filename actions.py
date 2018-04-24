#!/usr/bin/env python

from visual import *
from random import uniform
import math

def rotate(eqn, obj, dmn_1, dmn_2, dx, string, a1, a2, a3):
    if string == "y":
        if len(obj) == 0:

            col = color.yellow

            c = 128
            for _ in range(0,2*c):
                x = arange(dmn_1, dmn_2, dx)
                frm = frame()
                func = curve(frame = frm, x = x, y = eval(eqn), color = col, radius = 0.05)
                obj.append(frm)

            count = 1
            for _ in obj:
                rate(150)
                _.rotate(angle=count*math.pi/c, axis=(0,1,0))
                count += 1
        else:
            for _ in obj:
                rate(150)
                _.visible = False
                del _
            obj = []
    elif string == "x":
        if len(obj) == 0:

            col = color.yellow

            c = 128
            for _ in range(0,2*c):
                x = arange(dmn_1, dmn_2, dx)
                frm = frame()
                func = curve(frame = frm, x = x, y = eval(eqn), color = col, radius = 0.05)
                obj.append(frm)

            count = 1
            for _ in obj:
                rate(150)
                _.rotate(angle=-count*math.pi/c, axis=(1,0,0))
                count += 1
        else:
            for _ in obj:
                rate(150)
                _.visible = False
                del _
            obj = []
    elif string == "z":
        if len(obj) == 0:

            col = color.yellow

            c = 128
            for _ in range(0,2*c):
                x = arange(dmn_1, dmn_2, dx)
                frm = frame()
                func = curve(frame = frm, x = x, y = eval(eqn), color = col, radius = 0.05)
                obj.append(frm)

            count = 1
            for _ in obj:
                rate(150)
                _.rotate(angle=count*math.pi/c, axis=(0,0,1))
                count += 1
        else:
            for _ in obj:
                rate(150)
                _.visible = False
                del _
            obj = []
    elif string == "a":
        if len(obj) == 0:

            col = color.yellow

            c = 128
            for _ in range(0,2*c):
                x = arange(dmn_1, dmn_2, dx)
                frm = frame()
                func = curve(frame = frm, x = x, y = eval(eqn), color = col, radius = 0.05)
                obj.append(frm)

            count = 1
            for _ in obj:
                rate(150)
                _.rotate(angle=count*math.pi/c, axis=(a1,a2,a3))
                count += 1
        else:
            for _ in obj:
                rate(150)
                _.visible = False
                del _
            obj = []

    return obj
