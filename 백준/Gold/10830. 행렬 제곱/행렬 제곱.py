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
                mt[i][j]%=1000
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

a,b=map(int,input().split())
mt=[list(map(int,input().split())) for i in range(a)]
x=square(mt,b)
for i in range(a):
    for j in range(a):
        print(x[i][j]%1000, end=" ")
    print()

