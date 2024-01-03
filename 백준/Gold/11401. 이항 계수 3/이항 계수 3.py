import sys
import math
def input():return sys.stdin.readline().rstrip()
def fact(a):
    n=1
    for i in range(2,a+1):
        n=n*i%1000000007
    return n



def square(a,n):
    if n==1:
        return a
    if n%2==0:
        mt=square(a,n//2)
        return (mt*mt)%1000000007
    else:
        mt=square(a,n-1)
        return (mt*a)%1000000007

a,b=map(int,input().split())
b=min(b,a-b)
print(fact(a)*(square(fact(b)*fact(a-b),1000000007-2))%1000000007)

