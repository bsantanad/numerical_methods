import sympy as sp

def f(x,y):
    #return 2*x*y
    return (x+y-1)**2

x0 = 0
y0 = 2
h = 0.1
points = 5

x = sp.Symbol('x')
y = sp.Symbol('y')

#d2xy = 2*y + 2*x*f(x,y)
d2xy = 2*(x+y-1)*(f(x,y)+1)

yn = y0
xn = x0

for _ in range(points):
    yk = yn + f(xn,yn)*h \
         + d2xy.subs([(x,xn),(y,yn)]).evalf()*((h**2)/2)
    xk = xn + h
    print(f'{yk}')
    yn = yk
    xn = xk

