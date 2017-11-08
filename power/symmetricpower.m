function y = symmetricpower(A,x)
n = length(A);
TOL = 0.001;
N = 20; %maximum number of iteration
k = 1;
while k <= N
    y = A*x;
    u = x'*y;
    if norm(y) == 0
       print('Eigenvector', x);
       print('A has eigenvalue 0, select new vector x and restart');
       return;
    end
    
    err = norm(x-y./norm(y));
    x = y./norm(y);
    if err < TOL 
        u
        x
        return;
    end
    k = k + 1;
end

print('Maximum number of iterations exceeded');
