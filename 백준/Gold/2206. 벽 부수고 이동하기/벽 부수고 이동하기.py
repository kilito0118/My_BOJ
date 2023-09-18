from collections import deque
import sys
def input(): return sys.stdin.readline().rstrip()
dx=[0,0,1,-1]
dy=[1,-1,0,0]
q = deque(list())
a,b=map(int,input().split())
zido = [list(map(int,list(input()))) for i in range(a)]
check=[[0 for i in range(b)] for i in range(a)]
q.append(0)
q.append(0)
q.append(-1)
q.append(0)
ans1=[]
ans2=[]
while q:
	x=q.popleft()
	y=q.popleft()
	cnt=q.popleft()
	w=q.popleft()

	if x==a or y==b or x==-1 or y==-1:
		continue
	if w==1:
		if check[x][y]!=0:
			continue
	else:
		if zido[x][y]<0:
			continue
	if zido[x][y]==1:
		w+=1
	else:
		pass
		#print(x,y)
	if w==2:
		continue
	
	if x==a-1 and y==b-1:
		ans1.append(cnt)
	for i in range(4):
		q.append(x+dx[i])
		q.append(y+dy[i])
		q.append(cnt-1)
		q.append(w)
	if w==0:
		zido[x][y]=cnt
	else:
		check[x][y]=cnt
else:
	if len(ans1)==0:
		print(-1)
	else:
		print(-max(ans1))
#print(*zido,sep="\n")
		