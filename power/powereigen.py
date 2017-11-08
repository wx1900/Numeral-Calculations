import numpy as np
from numpy import linalg as LA

A = np.matrix( ((4.0000,-1.0000,1.0000),(-1.0000,3.0000,-2.0000),(1.0000,-2.0000,3.0000)))
# A = A.I; 
x = np.matrix('1;1;1')
TOL = 0.001
xn = A*x
xp = x
MAX_ITR = 20
k = 1
while k <= MAX_ITR :
    xp = xn
    y = max(abs(xn))
    xn = xn/y
    xn = A*xn
    if max(abs(xn-xp)) < TOL:
        print(xp)
        print(y)
        print(k)
        break 
    k = k+1
# print("\nMaximum number of iterations exceeded")