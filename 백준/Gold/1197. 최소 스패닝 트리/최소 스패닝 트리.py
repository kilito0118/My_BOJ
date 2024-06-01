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
        
def bfs(x):
    cnt = 0
    while q:
        xnt,x,y = heapq.heappop(q)
        if(set_find(x)==set_find(y)):
            continue
        set_union(x,y)
        cnt+=xnt
    else:
        print(cnt)
        exit()

a,b=map(int,input().split())
visit = [i for i in range(a+1)]
q = []
for i in range(b):
    x,y,cnt=map(int,input().split())
    heapq.heappush(q,(cnt,y,x))
    heapq.heappush(q,(cnt,x,y))
bfs(1)
