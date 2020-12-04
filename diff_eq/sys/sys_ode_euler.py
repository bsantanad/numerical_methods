import math 

def dx(t,x,y):
    return x+2*y
    #return y

def dy(t,x,y):
    return 3*x+2*y
    #return (math.sin(2*t)-4*dx(t,x,y)-x)/2
    #return -4*y+-5x

x = 6
y = 4
t = 0.05
h = 0.05
points = 5

xn = x
yn = y
tn = 0
for _ in range(points):
    print(f"{tn:0.2f}: {xn:.6f},{yn:.6f}")
    tk = tn + h
    xk = xn+h*dx(tn,xn,yn)
    yk = yn+h*dy(tn,xn,yn)
    xn = xk
    yn = yk
    tn = tk

print(f"{tn:0.2f}: {xn:.6f},{yn:.6f}")
