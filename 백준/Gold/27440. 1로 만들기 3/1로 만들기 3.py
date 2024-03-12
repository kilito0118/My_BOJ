import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()
a = int(input())

q = deque()
q.append((a,0))

check = dict()


while True:
    x,cnt = q.popleft()
    if x in check:
        continue
    #print(x)
    check[x] = cnt
    if x==1:
        print(cnt)
        break
    if x%3==0 and ((x//3) not in check):
        q.append((x//3,cnt+1))
    if x%2==0 and ((x//2) not in check):
        q.append((x//2,cnt+1))
    if x>=2 and ((x-1) not in check):
        q.append((x-1,cnt+1))
