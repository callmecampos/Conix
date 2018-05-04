#!/usr/bin/env python

# Conix, created 10/20/2016 by Felipe Campos

from ui import *

def main():
    one_eq, eqn, eqn1, eqn2, dmn1, dmn2, dx = initialize()

    auto = False

    if one_eq:
        finish = single(eqn,dmn1,dmn2,dx)
    else:
        finish = double(eqn1,eqn2,dx,auto,dmn1,dmn2)

    exit()

main()

# NOTES:

# donuts (pi * (r2 - r1) stuff) with two separate curves
# make two main functions (main, secondary) one with one curve and one with two curves for donut or whatever
#
# see if you can color in the portion under the curve to show the integral? rotating that as well might be difficult, but you should consider it (don't have to though)
# piecewise functions
# scene.forward = (q,w,a) --> start at (0,0,0) w/o zax then shift to (q,w,a)
#
# DO A DRAWING OF IDEAL MENU AND WORKFLOW AND STUFF ON WHITEBOARD
# e-mail vpython team about slow framerates with mouse and keyboard events or try googling a way around it for menu controls
