
def f(x,y):
    #return 3*(x**2)*y
    return (x+y-1)**2

x = 0
y = 2
h = 0.1
points = 5

xn = x
yn = y
for _ in range(points):
    pn = yn + h*f(xn,yn)
    xk = xn + h
    ynk = yn + (h/2)*(f(xn,yn)+f(xk,pn))
    xn = xk
    yn = ynk
    print(f"{xn:.6f},{yn:.6f}")
