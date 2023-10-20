import sys, heapq
def input():return sys.stdin.readline().rstrip()
a=int(input())
q=[int(input()) for i in range(a)]
heapq.heapify(q)
cnt=0

for i in range(a-1):
    x=heapq.heappop(q)
    y=heapq.heappop(q)
    heapq.heappush(q,x+y)
    cnt+=x+y
print(cnt)


