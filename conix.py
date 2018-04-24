#!/usr/bin/env python

# Conix, created 10/20/2016 by Felipe Campos

from visual import *
from random import uniform
from actions import rotate
from ui import *
import math

_rate = 100
one_eq,eqn,eqn1,eqn2,dmn1,dmn2,dx = True,'4','2','0',6,9,0.1

rate(_rate)

print("Welcome to Conix: An Integration Simulation\n")

val = -1
print("Please choose from one of the following equations:\n(1) y = x\n(2) y = x^3\n(3) y = (x-1)*(x-3)^2\n(4) Create your own equation")
while True:
    try:
        temp = int(raw_input("Choose a number corresponding with your intended option (1-4): "))
        if type(temp) == int and (0 < temp and temp < 4):
            val = temp
        else:
            val = int('krusty krab is unfair, mr krabs is in there, standing at concession, plotting his oppression')
        break
    except ValueError:
        print("Invalid response, please try again.")

if one_eq == True:
    if val == 1:
        eqn = 'x'
    elif val == 2:
        eqn = 'x**3'
    elif val == 3:
        eqn = '(x-1)*(x-3)**2'
    elif val == 4:
        # take a function f(x) and some domain (i.e. 1 to 3)
        # some example functions: '(x+2)*(x-3)**2', '(x-1)*(x-3)**2'

        # make instructions as to how to use the app (** vs ^, * for times, etc etc)
        # maybe make buttons in a menu along with a list of functions

        while True:
            try:
                eqn = raw_input("Enter any function y = ")
                if eqn.find("^") != -1: # or something else
                    print('Function inputted incorrectly, please try again.')
                else:
                    x = 1738
                    y_test = eval(eqn)
                    break
            except NameError:
                print('Function inputted incorrectly, please try again.')

    dmn1 = prompt("Enter the start of the domain: ", float, "Value error, please try again.", ValueError)
    dmn2 = prompt("Enter the end of the domain: ", float, "Value error, please try again.", ValueError)
    dx = prompt("Enter dx: ", float, "Value error, please try again.", ValueError)

    print eqn, "from", dmn1, "to", dmn2
    print "dx =", dx
else:
    if val == '2x^2 - 6x + 4, 4*cos(pi*x / 4)':
        eqn1, eqn2 = '2*x**2 - 6*x + 4', '4*cos(math.pi*x / 4)'
    elif val == '1 + x + e^(x^2 - 2x), x^4 - 6.5x^2 + 6x + 2':
        eqn1, eqn2 = '1 + x + e^(x**2 - 2*x)', 'x**4 - 6.5*x**2 + 6*x + 2'
    elif val == 'Select a pair of equations':
        eqn1, eqn2 = '', ''
        while True:
            try:
                eqn1 = raw_input("Enter any function y = ")
                if eqn1.find("^") != -1: # or something else
                    print('Function inputted incorrectly, please try again.')
                else:
                    x = 1738
                    y_test = eval(eqn1)
                    break
            except NameError:
                print('Function inputted incorrectly, please try again.')
        while True:
            try:
                eqn2 = raw_input("Enter any function y = ")
                if eqn2.find("^") != -1: # or something else
                    print('Function inputted incorrectly, please try again.')
                else:
                    x = 1738
                    y_test = eval(eqn2)
                    break
            except NameError:
                print('Function inputted incorrectly, please try again.')

    dmn1 = prompt("Enter the start of the domain: ", float, "Value error, please try again.", ValueError)
    dmn2 = prompt("Enter the end of the domain: ", float, "Value error, please try again.", ValueError)
    dx = prompt("Enter dx: ", float, "Value error, please try again.", ValueError)

    print eqn1, eqn2, "from", dmn1, "to", dmn2
    print "dx =", dx

auto = False

if one_eq == True:
    finish = single(eqn,dmn1,dmn2,dx)
else:
    finish = double(eqn1,eqn2,dx,auto,dmn1,dmn2)

exit()

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
