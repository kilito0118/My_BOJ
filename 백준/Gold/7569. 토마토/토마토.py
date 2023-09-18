import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()
a,b,c = map(int,input().split())
pan = [[input().split() for i in range(b)]for i in range(c)] 
#print(pan)
q = deque()
mcnt = 0
dx = [0,0,1,-1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

for z in range(c):
    for i in range(b):
        for j in range(a):
            if pan[z][i][j] == "1":
                q.append((z,i,j,0))
                pan[z][i][j] = "0"

while q:
    z,x,y,cnt = q.popleft()
    if x==b or y==a or x==-1 or y==-1 or z==-1 or z==c or pan[z][x][y]=='1' or pan[z][x][y]=='-1':
        
        continue
    pan[z][x][y]='1'
    
    cnt+=1
    mcnt=max(cnt,mcnt)
    for i in range(6):
        q.append((z+dz[i],x+dx[i],y+dy[i],cnt))
for z in range(c):
    for i in range(b):
        for j in range(a):
            if pan[z][i][j] == "0":
                print(-1)
                exit()

#print(pan)
print(mcnt-1)     
