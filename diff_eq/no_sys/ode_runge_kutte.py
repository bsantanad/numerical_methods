import numpy as np

def f(x,y):
    return (x+y-1)**2 

x0 = 0
y0 = 2
dx = 0.1
points = 5

xk = x0
yk = y0
data_rk = np.array([[xk, yk]])

print(yk)
for _ in range(points):
    k1 = dx*f(xk,yk)
    k2 = dx*f(xk+0.5*dx, yk+0.5*k1)
    k3 = dx*f(xk+0.5*dx, yk+0.5*k2)
    k4 = dx*f(xk+dx, yk+k3)
    yk = yk + (1/6.0)*(k1+2*k2+2*k3+k4)
    xk = xk + dx
    data2add = np.array([[xk,yk]])
    data_rk = np.concatenate((data_rk, data2add), axis=0) 
    print(yk)
