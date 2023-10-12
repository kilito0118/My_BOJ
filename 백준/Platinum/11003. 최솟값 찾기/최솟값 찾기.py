from collections import deque
import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
c = list(map(int,input().split()))

q=deque()

for i in range(a):
    if q and q[0][1]<=i-b:
        q.popleft()
        
    while q and q[-1][0]>c[i]:
        q.pop()
    q.append((c[i],i))
    print(q[0][0],end=" ")
