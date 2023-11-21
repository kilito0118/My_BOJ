import heapq
import sys
def input():return sys.stdin.readline().rstrip()

a,b,c=map(int,input().split())
zido=list(map(int,input().split()))

gra=[[] for i in range(a+1)]

for i in range(c):
    x,y,z=map(int,input().split())
    gra[x].append((z,y))
    gra[y].append((z,x))
mcnt=0
for i in range(1,a+1):
    q=[]
    cnt=0
    heapq.heappush(q,(0,i))
    nowzido=["" for i in range(a+1)]
    while(q):
        score,x=heapq.heappop(q)
        if score>b:
            continue
        if nowzido[x]=="":
            nowzido[x]=score
        else:
            continue
        for i in gra[x]:
            heapq.heappush(q,(i[0]+score,i[1]))
        cnt+=zido[x-1]
    mcnt=max(cnt,mcnt)
print(mcnt)
    
        
        
