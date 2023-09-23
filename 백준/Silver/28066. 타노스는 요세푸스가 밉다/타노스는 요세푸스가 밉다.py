import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()
a,b = map(int,input().split())
q = deque([i for i in range(1,a+1)])
while True:
    k = q.popleft()

    a-=1
    if a<b-1:
        print(k)
        exit()
    else:
        for i in range(b-1):
            q.popleft()
            #print(q)
        a+=1
        a-=(b-1)
        q.append(k)
        #print(q)
#print(q.popleft())
