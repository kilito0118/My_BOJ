import sys
from queue import PriorityQueue

def input():return sys.stdin.readline().rstrip()
a = int(input())
zido = [list(input()) for i in range(a)]
check = [[-1 for i in range(a)] for i in range(a)]
pq = PriorityQueue()
pq.put((0,0,0))#거리, 좌표
dx = [0,0,1,-1]
dy=[1,-1,0,0]

while not(pq.empty()):
	cnt,x,y,=pq.get()
	
	if x==a or y==a or x==-1 or y==-1 or check[x][y]!=-1:
		continue
	if zido[x][y]=='0':
		cnt+=1
	check[x][y]=cnt
	for i in range(4):
		pq.put((cnt,x+dx[i],y+dy[i]))
print(check[a-1][a-1])
	
	