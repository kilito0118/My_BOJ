import sys
def input():return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=map(int,input().split())
if (d-b)*e-(d-b)*a+b*(c-a)>f*(c-a):
    print(-1)
elif (d-b)*e-(d-b)*a+b*(c-a)<f*(c-a):
    print(1)
else:
    print(0)
