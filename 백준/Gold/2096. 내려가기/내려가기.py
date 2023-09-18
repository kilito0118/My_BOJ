import copy
import sys
def input() : return sys.stdin.readline().rstrip()
a = int(input())

c = list(map(int,input().split()))
d = copy.deepcopy(c)

for i in range(a-1):
    b = list(map(int,input().split()))
    x = copy.deepcopy(b)
    k=max(c)
    z = min(d)
    if k==c[1]:
        b[0]+=k
        b[1]+=k
        b[2]+=k
    
    else:
        b[1] +=k
        b[0]+=max(c[0],c[1])
        b[2]+=max(c[1],c[2])
    
    c = b
    if z==d[1]:
        x[0]+=z
        x[1]+=z
        x[2]+=z
    else:
        x[1]+=z
        x[0]+=min(d[0],d[1])
        x[2]+=min(d[1],d[2])
    d=x
print(max(c),min(d))

