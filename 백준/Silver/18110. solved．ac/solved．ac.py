import sys
def input():return sys.stdin.readline().rstrip()
def rd(a):
    if a-int(a)>=0.5:
        return int(a)+1
    else:
        return int(a)
a=int(input())
b=sorted([int(input()) for i in range(a)])
if a==0:
    print(0)
    exit()
k=rd(a*0.15)
#print(k)
print(rd(sum(b[k:a-k])/(a-2*k)))
