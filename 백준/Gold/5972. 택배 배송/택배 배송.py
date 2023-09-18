import sys
from queue import PriorityQueue

def input():return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
zido = [[] for i in range(a+1)]
check=[-1 for i in range(a+1)]
for i in range(b):
	x,y,z=map(int,input().split())
	zido[x].append((y,z))
	zido[y].append((x,z))
pq= PriorityQueue()
pq.put((0,1))
while not(pq.empty()):
	dis,x=pq.get()
	#print(dis,x)
	if check[x]==-1:
		check[x]=dis
	else:
		continue
	for i,j in zido[x]:
		pq.put((j+dis,i))
print(check[-1])
