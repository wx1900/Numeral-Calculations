import numpy as np
from numpy import linalg as LA

A = np.matrix( ((4,-1,1),(-1,3,-2),(1,-2,3)));
x = np.matrix('1;1;1');
xn = A*x;
xp = x;

print(A);
print(x);
print(xn);
print(xp);
print(max(abs(xn)));
print(max(abs(xn-xp)));