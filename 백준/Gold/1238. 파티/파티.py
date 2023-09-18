import sys
import heapq
def input():return sys.stdin.readline().rstrip()

a,b,c = map(int,input().split())
gra = [[] for i in range(a+1)]
for i in range(b):
    x,y,cnt = map(int,input().split())
    gra[x].append((cnt,y))
mcnt = 0

for i in range(1,a+1):
    check = [99999 for i in range(a+1)]
    q = []
    heapq.heapify(q)
    
    heapq.heappush(q,(0,i))
    #print(q)
    scnt = 0
    while q:
        cnt,x = heapq.heappop(q)
        if check[x]<cnt:
            continue
        check[x] = min(check[x],cnt)
        if x ==c:
            scnt = cnt
            break
        
        for j,k in gra[x]:
            heapq.heappush(q,(j+cnt,k))
            
    
    lcnt = 0
    q = []
    heapq.heapify(q)
    check = [99999 for i in range(a+1)]
    heapq.heappush(q,(0,c))
    
    while q:
        cnt,x = heapq.heappop(q)
        if check[x]<cnt:
            continue
        else:
            check[x] = min(check[x],cnt)
        if x ==i:
            
            lcnt = cnt
            break
        
        for j,k in gra[x]:
            heapq.heappush(q,(j+cnt,k))
        

    mcnt = max(mcnt,lcnt+scnt)
    
    #print(scnt,lcnt)
print(mcnt)

            