#!/usr/bin/env python

from vpython import *
from random import uniform
import math

# Rotate our equation around a given axis or random 3D vector
def rotate(eqn, obj, dmn_1, dmn_2, dx, a1, a2, a3):
    _axis = vector(a1, a2, a3)

    if len(obj) == 0:
        
        col = color.yellow

        c = 128
        for _ in range(0,2*c):
            x = arange(dmn_1, dmn_2, dx)
            
            lambda_eqn = lambda x : eval(eqn)

            vals = [[_x, lambda_eqn(_x), 0] for _x in x]

            func = curve(pos = vals, color = color.yellow, radius = 0.05)
            obj.append(func)

        count = 1
        for _ in obj:
            rate(150)
            _.rotate(angle=count*math.pi/c, axis=_axis)
            count += 1
    else:
        for _ in obj:
            rate(150)
            _.visible = False
            del _
        obj = []

    return obj
