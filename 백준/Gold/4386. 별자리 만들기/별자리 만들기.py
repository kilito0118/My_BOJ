import sys
import heapq

def input():return sys.stdin.readline().rstrip()

def set_find(k):
    if visit[k]==k:
        return k
    visit[k] = set_find(visit[k])
    return visit[k]
def set_union(q,w):
    q = set_find(q)
    w = set_find(w)
    if q>w:
        visit[q] = w
    else:
        visit[w] = q

a = int(input())
zido = [list(map(float,input().split())) for i in range(a)]
q = []
visit = [i for i in range(a+1)]
for i in range(a):
    for j in range(i+1,a):
        dx = (zido[i][0]-zido[j][0])**2
        dy = (zido[i][1]-zido[j][1])**2
        heapq.heappush(q,(dx+dy,i,j))
cnt = 0
while q:
    dis,x,y = heapq.heappop(q)
    if(set_find(x)==set_find(y)):
        continue
    set_union(x,y)
    cnt+=dis**0.5
print(cnt)
