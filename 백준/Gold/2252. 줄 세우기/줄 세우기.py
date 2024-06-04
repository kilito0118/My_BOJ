import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

zido = [[] for i in range(a+1)]
h = [0 for i in range(a+1)]
q = deque()

for i in range(b):
    x,y=map(int,input().split())
    zido[x].append(y)
    h[y] += 1
for i in range(1,a+1):
    if h[i]==0:
        q.append(i)
ans = []
while q:
    e = q.popleft()
    ans.append(e)
    for i in zido[e]:
        h[i]-=1
        if h[i]==0:
            q.append(i)
print(*ans)
