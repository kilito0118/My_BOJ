import heapq
import sys
def input():return sys.stdin.readline().rstrip()
 

a,b=map(int,input().split())

gra=[{} for i in range(a+1)]
for i in range(b):
    x,y,z=map(int,input().split())
    gra[x][y]=z
    gra[y][x]=z

s,e=map(int,input().split())

def dy(start,end):
    zido = [1000*1000 for i in range(a+1)]
    q=[]
    heapq.heappush(q,(0,start))
    while q:
        z,x = heapq.heappop(q)
        if zido[x]<z: continue
        zido[x]=z
        
        if x==end:
            return z
        for i in gra[x].items():
            heapq.heappush(q,(z+i[1],i[0]))
    else:
        return None

try:
    k=min(dy(1,s)+dy(e,a),dy(1,e)+dy(s,a))+dy(s,e)
    print(k)
except:
    print(-1)
