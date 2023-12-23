import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()
check = [0 for i in range(3000)]
q=deque()
a=int(input())
q.append((1,0,0))
q.append((1,1,1))
j = set()
j.add((1,0,0))
j.add((1,1,1))
while q:
    
    x,y,z=q.popleft()
    if x>2000:
        continue
    if x<=0:
        continue

    
    if x==a:
        print(y)
        break
    if (x-1,y+1,z) not in j:
        q.append((x-1,y+1,z))
        j.add((x-1,y+1,z))
    if (x+z,y+1,z) not in j:
        q.append((x+z,y+1,z))
        j.add((x+z,y+1,z))
    if (x,y+1,x) not in j:
        q.append((x,y+1,x))
        j.add((x,y+1,x))
    
    
    

