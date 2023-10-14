#@에서 bfs돌려서 출구 찾기
#아니면 바깥과 닿아있는 . 을 다 E로 바꿔서 출구로 만듦
#E에서 *까지의 거리와 @까지의 거리를 계산(1많으면 무조건 먼저 도달 가능)
from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]

for i in range(int(input())):
	q=deque(list())
	a,b=map(int,input().split())
	zido = []
	wili=(0,0)
	for j in range(b):
		k = list(input())
		zido.append(k)
		for x in range(a):
			if k[x]=='*':
				q.append(j)
				q.append(x)
				q.append(1)
				k[x]="."
			elif k[x]=="@":
				wili = (j,x)
				k[x]="."
	q.append(wili[0])
	q.append(wili[1])
	q.append(-1)
	while q:
		x = q.popleft()
		y = q.popleft()
		cnt=q.popleft()
		#print(x,y)
		if x==-1 or y==-1 or x==b or y==a or zido[x][y]!=".":
			continue
		if x==0 or y==0 or x==b-1 or y==a-1:
			if cnt>0:
				
				pass
			else:
				#print(*zido,sep="\n")
				print(-cnt)
				break
		
		
		

		#print(x,y,cnt)
		for i in range(4):
			q.append(x+dx[i])
			q.append(y+dy[i])
			if cnt<0:
				q.append(cnt-1)
			else:
				q.append(cnt+1)
		zido[x][y]=cnt
		
		
	
	else:
		print('IMPOSSIBLE')
	
	
	
	
