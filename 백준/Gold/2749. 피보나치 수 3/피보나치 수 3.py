import sys
def input(): return sys.stdin.readline().rstrip()
def mt_mult(a,b):
    x = len(a)
    y = len(b)
    mt=[[0 for i in range(x)] for i in range(y)]
    for i in range(x):
        for j in range(x):
            for k in range(y):
                mt[i][j]+=a[i][k]*b[k][j]
                mt[i][j]%=1000000
    return mt
def square(a,n):
    if n==1:
        return a
    if n%2==0:
        mt=square(a,n//2)
        return mt_mult(mt,mt)
    else:
        mt=square(a,n-1)
        return mt_mult(mt,a)

a=int(input())
mt=[[1,1],[1,0]]

x=square(mt,a)
print(x[0][1])