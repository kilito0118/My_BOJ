import sys
def input():return sys.stdin.readline().rstrip()
import heapq

a,b=map(int,input().split())
zido=[list(map(int,list(input()))) for i in range(b)]

check = [[-1 for i in range(a)] for i in range(b)]

dx=[0,1,0,-1]
dy=[1,0,-1,0]

q=[]

heapq.heappush(q,(0,0,0))

while(q):
    cnt,x,y = heapq.heappop(q)
    
    if b==x or a==y or x==-1 or y==-1:
        continue
    if zido[x][y]==1:
        cnt+=1
    if check[x][y]!=-1:
        continue
    check[x][y] = cnt
    if x==a-1 and y==b-1:
        break
    for i in range(4):
        heapq.heappush(q,(cnt,x+dx[i],y+dy[i]))
print(check[b-1][a-1])
