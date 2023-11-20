import heapq
import sys
def input():return sys.stdin.readline().rstrip()
 

a,b=map(int,input().split())

gra=[[] for i in range(a+1)]
for i in range(b):
    x,y,z=map(int,input().split())
    gra[x].append((z,y))
    gra[y].append((z,x))

s,e=map(int,input().split())

def dy(start,end):
    vist = [0 for i in range(a+1)]
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        z,x = heapq.heappop(q)
        if vist[x]==1:
            continue
        else:
            vist[x]=1
        if x==end:
            return z
        for i in gra[x]:
            heapq.heappush(q,(z+i[0],i[1]))
    else:
        return None
try:
    k=min(dy(1,s)+dy(e,a),dy(1,e)+dy(s,a))+dy(s,e)
    print(k)
except:
    print(-1)
