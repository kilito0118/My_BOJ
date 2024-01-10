import sys
import heapq
def input(): return sys.stdin.readline().rstrip()

a=int(input())

sulist = sorted([list(map(int,input().split())) for i in range(a)],key=lambda x: x[1])
q=[]
cnt=0

for i in sulist:
    p,d=i
    heapq.heappush(q,p)
    cnt+=1
    if d<cnt:
        heapq.heappop(q)
        cnt-=1

print(sum(q))

