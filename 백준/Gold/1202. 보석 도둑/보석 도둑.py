#가치있는 순-> 가장 가벼운 가방에 넣기
from collections import deque
import heapq
import sys
def input():return sys.stdin.readline().rstrip()

a,b=map(int,input().split())

jew=[]
for i in range(a):
    x,y=map(int, input().split())
    jew.append((x,y))
jew.sort(key=lambda x : (x[0],-x[1]))


s=sorted([int(input()) for i in range(b)])
pq = []

cnt=0
su=0
#print(s)
#print(jew)

for i in range(b):
    
    while True:
        
        if cnt>=a or s[i]<jew[cnt][0]:
            break
        else:
            heapq.heappush(pq,-jew[cnt][1])
            cnt+=1
    if pq:
        su+=heapq.heappop(pq)
print(-su)
