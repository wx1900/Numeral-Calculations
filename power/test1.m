A = [4,-1,1;-1,3,-2;1,-2,3];
x = [1;1;1];
S1 = '----powereigen----';
S2 = '----inverse powereigen----';
S3 = '----symmetric powereigen----';
disp(S1)
y = powereigen(A,x);
AF = pinv(A);
disp(S2)
z = powereigen(AF,x);
disp(S3)
symmetricpower(A,x);