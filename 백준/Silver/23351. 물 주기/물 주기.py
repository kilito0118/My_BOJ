import sys
def input():return sys.stdin.readline().rstrip()

n,k,a,b=map(int,input().split())
#a는 연속 수 b는 물 양
pot=[k for i in range(n)]
ind=min(pot)
cnt=0
while True:
    cnt+=1
    j=pot.index(ind)
    if j>n-a:
        j=n-a
    for i in range(a):
        pot[j+i]+=b
    for i in range(n):
        pot[i]-=1
    ind=min(pot)
    #print(pot)
    if ind==0:
        print(cnt)
        break
        
    
