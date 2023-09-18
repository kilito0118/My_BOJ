import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()
a,b = map(int,input().split())
pan = [input().split() for i in range(b)]
q = deque()
mcnt = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for i in range(b):
    for j in range(a):
        if pan[i][j] == "1":
            q.append((i,j,0))
            pan[i][j] = "0"

while q:
    x,y,cnt = q.popleft()
    if x==b or y==a or x==-1 or y==-1 or pan[x][y]=='1' or pan[x][y]=='-1':
        
        continue
    pan[x][y]='1'
    
    cnt+=1
    mcnt=max(cnt,mcnt)
    for i in range(4):
        q.append((x+dx[i],y+dy[i],cnt))

for i in range(b):
    for j in range(a):
        if pan[i][j] == "0":
            print(-1)
            exit()


print(mcnt-1)     
