import sys
import math
def input():return sys.stdin.readline().rstrip()

a=int(input())
b=[int(input()) for i in range(a)]
c=[]
for i in range(1,a):
    c.append(abs(b[i-1]-b[i]))

k = math.gcd(*c)
an = set([k])
for i in range(2,int(k**(1/2))+1):
    if k%i==0:
        an.add(i)
        an.add(k//i)

    
print(*sorted(an),sep=" ")

