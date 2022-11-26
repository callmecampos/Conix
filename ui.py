#!/usr/bin/env python

from vpython import *
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

    scene = canvas(title='Conical Shells', x=0, y=0, color=color.gray)
    scene.background = vector(0.5,0.5,0.5)
    scene.forward = vector(q,w,a)
    scene.range = dmn_2*5

    # NOTE: websocket server gets started here... need to figure out a way to initialize this only when symbolica queries basically... so like it doesn't open...?

    xax = arrow(pos = vector(-dmn_2*25,0,0), axis = vector(50*dmn_2,0,0), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.blue)#, materials = materials.chrome)
    yax = arrow(pos = vector(0,-dmn_2*25,0), axis = vector(0,50*dmn_2,0), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.green)#, materials = materials.chrome)
    zax = arrow(pos = vector(0,0,-dmn_2*25), axis = vector(0,0,50*dmn_2), height = 0.25, depth = 0.25, shaftwidth = 0.1, color = color.red)#, materials = materials.chrome)

    x_label = label(pos = vector(dmn_2*3,0,0), text='x axis', yoffset=5, height=10, border=3, font='sans')
    y_label = label(pos = vector(0,dmn_2*3,0), text='y axis', yoffset=5, height=10, border=3, font='sans')
    z_label = label(pos = vector(0,0,dmn_2*3), text='z axis', yoffset=5, height=10, border=3, font='sans')

    # plot the function as a curve object

    x = arange(dmn_1, dmn_2, 0.01)

    # TODO: take in input from Symbolica and evaluate using sympy!!! and then visualize over http -- and use server to take inputs...

    lambda_eqn = lambda x : eval(eqn)

    vals = [[_x, lambda_eqn(_x), 0] for _x in x]

    func = curve(pos = vals, color = color.yellow, radius = 0.05)

    scene.conix_objects_y = []
    scene.conix_objects_x = []

    # generate cylindrical shells of random color and of volume = 2 * pi * x * f(x) * dx going from the beginning to the end of the range
    
    for x in arange(dmn_1, dmn_2, dx):
        rate(150)
        r = uniform(0,1)
        g = uniform(0,1)
        b = uniform(0,1)
        y_val = eval(eqn)

        pos_y = y_val

        cyl_y = cylinder(pos = vector(0,0,0), axis = vector(0,y_val,0), radius = x, color = vector(r,g,b), opacity = 0.15)
        cyl_y.visible = False

        cyl_x = cylinder(pos = vector(0,0,0), axis = vector(x,0,0), radius = y_val, color = vector(r,g,b), opacity = 0.15)
        cyl_x.visible = False

        scene.conix_objects_y.append(cyl_y)
        scene.conix_objects_x.append(cyl_x)

        if scene.range <= y_val / 1.5:
            scene.range = y_val+15
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

    flabel = label(pos=vector(dmn_2,pos_y,0), text="y = "+str(eqn), xoffset=offx, yoffset=offy, height=10, border=6, font='sans') # equation label

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

    scene.conix_ix = 0
    scene.conix_iy = 0

    scene.conix_q = True
    scene.conix_brk = False

    scene.conix_obj = []

    scene.conix_y_show = True
    scene.conix_x_show = True

    # (boolean on or off type thing --> return value of rotate()?)
    def keyEvent(evt):
        k = evt.key
        print(k)

        if (k == 'shift+down' or k == "(") and scene.range < rangemax:
            scene.range = scene.range + .5
        elif (k == 'shift+up' or k == "&") and scene.range > rangemin:
            scene.range = scene.range - .5
        elif k == 'up':
            scene.forward = vector(scene.forward.x, scene.forward.y - .1, scene.forward.z)
        elif k == 'down':
            scene.forward = vector(scene.forward.x, scene.forward.y + .1, scene.forward.z)
        elif k == 'right':
            scene.forward = vector(scene.forward.x - .1, scene.forward.y, scene.forward.z)
        elif k == 'left':
            scene.forward = vector(scene.forward.x + .1, scene.forward.y, scene.forward.z)
        elif k == 'shift+left' or k == '"':
            scene.forward = vector(scene.forward.x, scene.forward.y, scene.forward.z - .1)
        elif k == 'shift+right' or k == '%':
            scene.forward = vector(scene.forward.x, scene.forward.y, scene.forward.z + .1)
        elif k == 'i':
            scene.conix_objects_y[scene.conix_iy].visible = False
            if scene.conix_iy > 0:
                scene.conix_iy -= 1
            else:
                scene.conix_x_show = True
        elif k == 'o' and scene.conix_y_show:
            scene.conix_x_show = False
            scene.conix_objects_y[scene.conix_iy].visible = True
            if scene.conix_iy < len(scene.conix_objects_y) - 1:
                scene.conix_iy += 1
        elif k == 'I':
            scene.conix_objects_x[scene.conix_ix].visible = False
            if scene.conix_ix > 0:
                scene.conix_ix -= 1
            else:
                scene.conix_y_show = True
        elif k == 'O' and scene.conix_x_show:
            scene.conix_y_show = False
            scene.conix_objects_x[scene.conix_ix].visible = True
            if scene.conix_ix < len(scene.conix_objects_x) - 1:
                scene.conix_ix += 1
        elif k == 'r':
            a = 0
            c = 64
            while a != 2*c:
                rate(50)
                func.rotate(angle=math.pi/c, axis=vector(0,1,0))
                a += 1
        elif k == 'x' and scene.conix_x_show:
            scene.conix_obj = rotate(eqn,scene.conix_obj,dmn_1,dmn_2,0.01,1,0,0)
        elif k == 'y' and scene.conix_y_show:
            scene.conix_obj = rotate(eqn,scene.conix_obj,dmn_1,dmn_2,0.01,0,1,0)
        elif k == 'z':
            scene.conix_obj = rotate(eqn,scene.conix_obj,dmn_1,dmn_2,0.01,0,0,1)
        elif k == ' ':
            v1, v2, v3 = uniform(-10,10), uniform(-10,10), uniform(-10,10)
            scene.conix_obj = rotate(eqn,scene.conix_obj,dmn_1,dmn_2,0.01,v1,v2,v3)
        elif k == 'q':
            q = False
            scene.conix_brk = True
        elif k == '.':
            scene.conix_brk = True

    scene.bind('keydown', keyEvent)
    while scene.conix_brk == False:
        rate(100)
        #ks = keysdown()
        #if ks: print(ks)

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
                res = type_cast(input(request + " "))
                break
            except err_type:
                print(err)
        else:
            try:
                res = type_cast(input(request + " "))
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
            temp = int(input("Choose a number corresponding with your intended option (1-4): "))
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
                    eqn = input("Enter any function y = ")
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
                    eqn1 = input("Enter any function y_1 = ")
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
                    eqn2 = input("Enter any function y_2 = ")
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
