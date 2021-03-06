#!/usr/bin/env python

from visual import *
from random import uniform
from actions import rotate
import math

# MARK: Visual

# Plot a single equation
def single(eqn,dmn_1,dmn_2,dx):

    # set up the scene (axes, labels, etc.)

    q = -2
    w = -3
    a = -4

    scene = display(title='Conical Shells', x=0, y=0)
    scene.background = (0.5,0.5,0.5)
    scene.forward = (q,w,a)
    scene.range = (dmn_2*5,dmn_2*5,dmn_2*5)

    xax = arrow(pos = (-dmn_2*25,0,0), axis = (50*dmn_2,0,0), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.blue, materials = materials.chrome)
    yax = arrow(pos = (0,-dmn_2*25,0), axis = (0,50*dmn_2,0), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.green, materials = materials.chrome)
    zax = arrow(pos = (0,0,-dmn_2*25), axis = (0,0,50*dmn_2), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.red, materials = materials.chrome)

    x_label = label(pos = (dmn_2*3,0,0), text='x axis', yoffset=5, height=10, border=3, font='sans')
    y_label = label(pos = (0,dmn_2*3,0), text='y axis', yoffset=5, height=10, border=3, font='sans')
    z_label = label(pos = (0,0,dmn_2*3), text='z axis', yoffset=5, height=10, border=3, font='sans')

    # plot the function as a curve object

    x = arange(dmn_1, dmn_2, 0.01)

    f = frame()

    func = curve(frame = f, x = x, y = eval(eqn), color = color.yellow, radius = 0.05)

    objects_y = []
    objects_x = []

    # generate cylindrical shells of random color and of volume = 2 * pi * x * f(x) * dx going from the beginning to the end of the range
    
    for x in arange(dmn_1, dmn_2, dx):
        rate(150)
        r = uniform(0,1)
        g = uniform(0,1)
        b = uniform(0,1)
        y_val = eval(eqn)

        pos_y = y_val

        cyl_y = cylinder(pos = (0,0,0), axis = (0,y_val,0), radius = x, color = (r,g,b), opacity = 0.15)
        cyl_y.visible = False

        cyl_x = cylinder(pos = (0,0,0), axis = (x,0,0), radius = y_val, color = (r,g,b), opacity = 0.15)
        cyl_x.visible = False

        objects_y.append(cyl_y)
        objects_x.append(cyl_x)

        if scene.range.y <= y_val / 1.5:
            scene.range = (y_val+15,y_val+15,y_val+15)
            xax.shaftwidth += 0.1
            yax.shaftwidth += 0.1
            zax.shaftwidth += 0.1

    # create an array of values which corresponds to the integrand 2 * pi * x * f(x)

    func_yax = []
    x_arr = []

    eqn_tot = 'x*'+eqn

    for x in arange(dmn_1, dmn_2, 0.01):
        y_val = eval(eqn_tot)
        func_yax.append(y_val)
        x_arr.append(x)

    # create an array which corresponds to the integrand 2 * pi * f(x)

    func_xax = []

    for x in arange(dmn_1, dmn_2, 0.01):
        y_val = eval(eqn)
        func_xax.append(y_val)

    offx = 30 - dmn_2
    offy = 30 - pos_y

    flabel = label(pos=(dmn_2,pos_y,0), text="y = "+str(eqn), xoffset=offx, yoffset=offy, height=10, border=6, font='sans') # equation label

    # Turns off the default user spin and zoom and handles these functions itself.
    # This gives more control to the program and addresses the problem that at the time of writing,
    # Visual has a hidden user scaling variable that makes it impossible to force the camera position
    # by setting range, if the user has already zoomed using the mouse.

    # As a demonstration of this, press "f" or "g" to change the range, before or after zooming.
    # Use the following keys to change the orientation of the camera: "w", "a", "s", "d", "q", "e"
    # Use the "i" and "o" keys to go forwards and backwards in the creation of the integrated cylinders
    # Press the 'v' key to rotate the curve about the y-axis

    scene.userzoom = False
    scene.userspin = False
    rangemin = 1
    rangemax = 100

    i_x = 0
    i_y = 0

    q = True
    brk = False

    obj = []

    x_show = True
    y_show = True

    # (boolean on or off type thing --> return value of rotate()?)

    while brk == False:
        rate(100)
        if scene.kb.keys:
            k = scene.kb.getkey()

            if k == 'shift+down' and scene.range.x < rangemax:
                scene.range = scene.range.x + .5
            elif k == 'shift+up' and scene.range.x > rangemin:
                scene.range = scene.range.x - .5
            elif k == 'up':
                scene.forward = (scene.forward.x, scene.forward.y - .1, scene.forward.z)
            elif k == 'down':
                scene.forward = (scene.forward.x, scene.forward.y + .1, scene.forward.z)
            elif k == 'right':
                scene.forward = (scene.forward.x - .1, scene.forward.y, scene.forward.z)
            elif k == 'left':
                scene.forward = (scene.forward.x + .1, scene.forward.y, scene.forward.z)
            elif k == 'shift+left':
                scene.forward = (scene.forward.x, scene.forward.y, scene.forward.z - .1)
            elif k == 'shift+right':
                scene.forward = (scene.forward.x, scene.forward.y, scene.forward.z + .1)
            elif k == 'i':
                objects_y[i_y].visible = False
                if i_y > 0:
                    i_y -= 1
                else:
                    x_show = True
            elif k == 'o' and y_show == True:
                x_show = False
                objects_y[i_y].visible = True
                if i_y < len(objects_x) - 1:
                    i_y += 1
            elif k == 'I':
                objects_x[i_x].visible = False
                if i_x > 0:
                    i_x -= 1
                else:
                    y_show = True
            elif k == 'O' and x_show == True:
                y_show = False
                objects_x[i_x].visible = True
                if i_x < len(objects_x) - 1:
                    i_x += 1
            elif k == 'r':
                a = 0
                c = 64
                while a != 2*c:
                    rate(50)
                    f.rotate(angle=math.pi/c, axis=(0,1,0))
                    a += 1
            elif k == 'x' and x_show == True:
                obj = rotate(eqn,obj,dmn_1,dmn_2,0.01,"x",0,0,0)
            elif k == 'y' and y_show == True:
                obj = rotate(eqn,obj,dmn_1,dmn_2,0.01,"y",0,0,0)
            elif k == 'z':
                obj = rotate(eqn,obj,dmn_1,dmn_2,0.01,"z",0,0,0)
            elif k == ' ':
                v1, v2, v3 = uniform(-10,10), uniform(-10,10), uniform(-10,10)
                obj = rotate(eqn,obj,dmn_1,dmn_2,0.01,"a",v1,v2,v3)
            elif k == 'q':
                q = False
                brk = True
            elif k == '.':
                brk = True

    window.delete_all()

    return q

# Plot two equations
def double(eqn1,eqn2,dx,auto,dmn_1,dmn_2):
    # double curves (donut method)

    # ask for two curves
    # find where the curves intersect (possibly more than two)
    # figure out which curve is above the other on discrete intervals
    # fill in those areas (integrate)
    # rotate everything about the x-axis

    print("Still in beta, gang gang.")

    return True

# MARK: Prompt Setup

def prompt(request, type_cast=int, err="Error, please try again.", err_type=ValueError):
    res = None
    while True:
        if err_type != None:
            try:
                res = type_cast(raw_input(request + " "))
                break
            except err_type:
                print(err)
        else:
            try:
                res = type_cast(raw_input(request + " "))
                break
            except:
                print(err)
    return res

# Set up our equations, domains, ranges, dx, etc. for 3D display
def initialize():
    _rate = 100
    one_eq,eqn,eqn1,eqn2,dmn1,dmn2,dx = True,'4','2','0',6,9,0.1

    rate(_rate)

    print("Welcome to Conix: An Integration Simulation\n")

    val = -1
    if one_eq:
        print("Please choose from one of the following equations:\n \
              (1) y = x\n \
              (2) y = x^3\n \
              (3) y = (x-1)*(x-3)^2\n \
              (4) Create your own equation")
    else:
        print("Please choose from one of the following equation pairs:\n \
              (1) y_1 = 2x^2 - 6x + 4, y_2 = 4*cos(pi*x / 4)\n \
              (2) y_1 = 1 + x + e^(x^2 - 2x), y_2 = x^4 - 6.5x^2 + 6x + 2\n \
              (3) Create your own pair of equations (NOT SUPPORTED).")
    while True:
        try:
            temp = int(raw_input("Choose a number corresponding with your intended option (1-4): "))
            if type(temp) == int and (0 < temp and temp <= 4):
                val = temp
            else:
                val = int('krusty krab is unfair, mr krabs is in there, standing at concession, plotting his oppression')
            break
        except ValueError:
            print("Invalid response, please try again.")

    if one_eq:
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

        print(eqn + " from " + str(dmn1) + " to " + str(dmn2))
        print("dx = " + str(dx))
    else:
        if val == 1:
            eqn1, eqn2 = '2*x**2 - 6*x + 4', '4*cos(math.pi*x / 4)'
        elif val == 2:
            eqn1, eqn2 = '1 + x + e^(x**2 - 2*x)', 'x**4 - 6.5*x**2 + 6*x + 2'
        elif val == 3:
            eqn1, eqn2 = '', ''
            while True:
                try:
                    eqn1 = raw_input("Enter any function y_1 = ")
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
                    eqn2 = raw_input("Enter any function y_2 = ")
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

        print(eqn1 + " " + eqn2 + " from " + str(dmn1) + " to " + str(dmn2))
        print("dx = " + str(dx))

    return one_eq, eqn, eqn1, eqn2, dmn1, dmn2, dx
