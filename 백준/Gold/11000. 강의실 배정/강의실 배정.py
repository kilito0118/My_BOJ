import sys
import heapq
def input(): return sys.stdin.readline().strip()

s = sorted([list(map(int,input().split())) for i in range(int(input()))])
#print(s)
q=[0]
heapq.heapify(q)

cnt=1
for i,j in s:
    if q[0]<=i:
        heapq.heappushpop(q,j)
    else:
        heapq.heappush(q,j)
        cnt+=1

    
print(cnt)
