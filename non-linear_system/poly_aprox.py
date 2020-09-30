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

#fx = sp.cos(x)
fx = math.e**x
#fx = sp.sin(x) + sp.cos(2*x)
max_iter = 5
x0 = 0

###############
## Algorithm #
###############
pn = 0
fxprime = fx
for i in range(0,max_iter):
    feval = fxprime.evalf(subs={x: x0})
    fact = math.factorial(i)
    wx = (x-x0)**i
    pn += (feval/fact)*(wx) 
    fxprime = fx.diff(x)
    fx = fxprime
    #print(pn)


print(pn)
