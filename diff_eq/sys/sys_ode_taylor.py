import sympy as sp
import math

def dx(t,x,y):
    return x+2*y
    #return y

def dy(t,x,y):
    return 3*x+2*y 
    #return (sp.sin(2*t)-4*dx(t,x,y)-x)/2

x0 = 6
y0 = 4
t0 = 0.05
h = 0.05
points = 5

x = sp.Symbol('x')
y = sp.Symbol('y')
t = sp.Symbol('t')


d2x = dx(t,x,y) + 2*dy(t,x,y)
d2y = 3*dx(t,x,y) + 2*dy(t,x,y)

yn = y0
xn = x0
tn = 0

for _ in range(points):
    print(f"{xn:.8f},{yn:.8f}")
    #print(yn)
    tk = tn + h
    xk = xn + dx(tn,xn,yn)*h \
         + d2x.subs([(x,xn),(y,yn)]).evalf()*((h**2)/2)
    yk = yn + dy(tn,xn,yn)*h \
         + d2y.subs([(x,xn),(y,yn)]).evalf()*((h**2)/2)
    yn = yk.subs([(t,tn)])
    xn = xk.subs([(t,tn)])
    tn = tk
print(f"{xn:.8f},{yn:.8f}")
