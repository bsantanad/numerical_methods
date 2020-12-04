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
    print(f"{xn:.8f},{yn:.8f}")
    tk = tn + h

    k1x = h*dx(tn,xn,yn)
    k2x = h*dx(tn+(h/2), xn+(k1x/2), yn)
    k3x = h*dx(tn+(h/2), xn+(k2x/2), yn)
    k4x = h*dx(tn+h, xn+k3x, yn)
    xk = xn + (1/6)*(k1x + 2*k2x + 2*k3x + k4x)

    k1y = h*dy(tn,xn,yn)
    k2y = h*dy(tn+(h/2), xn, yn+(k1y/2))
    k3y = h*dy(tn+(h/2), xn, yn+(k2y/2))
    k4y = h*dy(tn+h, xn, yn+k3y)
    yk = yn + (1/6)*(k1y + 2*k2y + 2*k3y + k4y)
    
    xn = xk
    yn = yk
    tn = tk
print(f"{xn:.8f},{yn:.8f}")
