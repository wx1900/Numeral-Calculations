import numpy as np
from numpy import linalg as LA

A = np.matrix( ((4.0000,-1.0000,1.0000),
                (-1.0000,3.0000,-2.0000),
                (1.0000,-2.0000,3.0000)))
x = np.matrix('1;1;1')
TOL = 0.001
MAX_ITR = 20 # maximum number of iteration
k = 1
while k<=MAX_ITR:
    y = A*x
    u = x.T*y
    if LA.norm(y) == 0:
        print('Eigenvector')
        print(x)
        print('A has eigenvalue 0, select new vector x and restart');
        break
    
    err = LA.norm(x-y/LA.norm(y))
    x = y/LA.norm(y)
    if err < TOL:
        print(u)
        print(x)
        break

    k = k + 1

print('END.')
