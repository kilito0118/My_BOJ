import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

dx = [0,0,-1,1]
dy = [1,-1,0,0]

a,b = map(int,input().split())
q = deque()

zido = [list(map(int,input().split())) for i in range(a)]

q.append((0,0))

cnt=-1
while True:
    check = [[0 for i in range(b)] for i in range(a)]
    q = deque()
    q.append((0,0))
    cnt+=1
    while q:
        y,x = q.popleft()
        #print(y,x)
        if x==a or x==-1 or y==b or y==-1 or (check[x][y] >= 1 and zido[x][y] == 0):
            continue
        check[x][y]+=1
        if zido[x][y] == 0:
            for i in range(4):
                q.append((y+dy[i],x+dx[i]))
        


    x = 0
    for i in range(a):
        for j in range(b):
            if check[i][j] >=2:
                zido[i][j] = 0
                x+=1
    if x==0:
        break
print(cnt)
    

    
        



#print(*zido,sep="\n")

