import sys
def input():return sys.stdin.readline().rstrip()

a,b=map(int,input().split())
fi=[0 for i in range(a)]
for i in range(a):
    c=int(input())
    d=list(map(int,input().split()))
    for j in range(c):
        
        fi[i]=max(fi[i],(d[j*2]**2+d[j*2+1]**2)**(1/2))

    
print("%0.2f"%(sorted(fi)[b-1]**2))
