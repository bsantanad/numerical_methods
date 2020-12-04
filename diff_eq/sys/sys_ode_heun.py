import math

def dx(t,x,y):
    return x+2*y
    #return y

def dy(t,x,y):
    return 3*x+2*y
    #return (math.sin(2*t)-4*dx(t,x,y)-x)/2

x = 6
y = 4
t = 0.05
h = 0.05
points = 5

xn = x
yn = y
tn = 0
for _ in range(points):
    print(f"{xn:.6f},{yn:.6f}")
    tk = tn + h
    pn = xn + h*dx(tn,xn,yn)
    qn = yn + h*dy(tn,xn,yn)
    xk = xn + (h/2)*(dx(tn,xn,yn)+dx(tk,pn,yn))
    yk = yn + (h/2)*(dy(tn,xn,yn)+dy(tk,xn,qn))
    xn = xk
    yn = yk
    tn = tk

print(f"{xn:.6f},{yn:.6f}")
