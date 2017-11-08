function y = powereigen(A,x)
% use powereigen method to get the max characteristic 
% A = []
% x =[1;1;1]
% y = powereigen(A,x)

tol = 0.001;
xn = A*x
xp = x
k = 1
while max(abs(xn-xp))>tol
     xp = xn
     y = max(abs(xn)) 
     xn = xn./y
     xn = A*xn
     k = k+1
end
%display
xp
y
end