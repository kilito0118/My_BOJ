import sys
import heapq
def input():return sys.stdin.readline().rstrip()

a=int(input())
q=[]
for i in range(a):
    x,y,z=map(int,input().split())
    heapq.heappush(q,(y,z))

cnt=1

loom=[]
heapq.heappush(loom,0)
for i in range(a):
    s,e=heapq.heappop(q)
    x = heapq.heappop(loom)
    if x>s:
        cnt+=1
        heapq.heappush(loom,x)
    heapq.heappush(loom,e)
print(cnt)
        
