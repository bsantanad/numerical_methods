import numpy as np

def f1(x,y):
  return 3*x**2 + 2*y -4
def f2(x,y):
  return 2*x - 4*np.cos(y)

def jacob(x,y):
  return np.mat([[6*x, 2],[2, 4*np.sin(y)]])

vectork = (-1,3)
tol = 1e-9
max_iter = 100

for i in range(max_iter):
  jxk = np.linalg.inv(jacob(vectork[0], vectork[1]))
  fxk = [[f1(vectork[0],vectork[1])], [f2(vectork[0],vectork[1])]]
  xk = np.mat([[vectork[0]], [vectork[1]]]) - jxk*fxk
  vectork = (xk.item(0), xk.item(1))
  print(vectork)
