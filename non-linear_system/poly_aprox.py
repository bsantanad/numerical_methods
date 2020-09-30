'''
/usr/bin/pyhton3.7

A little code that uses sympy to make a 
polynomial aproximation :)

author: Benjamin Santana

'''
import sympy as sp
import numpy as np
import math

##################
## Symbols #######
#################

x = sp.Symbol('x')

##################
## Input #####
##################

fx = sp.cos(x)
max_iter = 15
x0 = 0

###############
## Algorithm #
###############
pn = 0
for i in range(0,max_iter):
    fxprime = fx.diff(x)
    #print(fxprime)
    feval = fxprime.evalf(subs={x: x0})
    fact = math.factorial(i)
    wx = (x-x0)**i
    pn += (feval/fact)*(wx) 
    fx = fxprime
    #print(pn)


print(pn)
