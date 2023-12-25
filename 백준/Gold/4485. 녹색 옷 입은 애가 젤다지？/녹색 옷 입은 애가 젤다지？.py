import sys
def input():return sys.stdin.readline().rstrip()
import heapq
qqqqq = 0
while True:
    a=int(input())
    if a==0:
        break
    qqqqq+=1
    zido=[list(map(int,input().split())) for i in range(a)]

    check = [[-1 for i in range(a)] for i in range(a)]

    dx=[0,1,0,-1]      
    dy=[1,0,-1,0]

    q=[]

    heapq.heappush(q,(0,0,0))

    while(q):
        cnt,x,y = heapq.heappop(q)
        
        if a==x or a==y or x==-1 or y==-1:
            continue
        
        cnt+=zido[x][y]
        if check[x][y]!=-1:
            continue
        check[x][y] = cnt
        if x==a-1 and y==a-1:
            continue
        for i in range(4):
            heapq.heappush(q,(cnt,x+dx[i],y+dy[i]))
    print("Problem {}: {}".format(qqqqq,check[a-1][a-1]))

