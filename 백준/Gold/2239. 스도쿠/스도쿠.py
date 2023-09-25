import sys 
#sys.setrecursionlimit(2500000)
def input(): return sys.stdin.readline().rstrip()

pan = [list(map(int,list(input()))) for i in range(9)]
zero=[]
for i in range(9):
	for j in range(9):
		if pan[i][j]==0:
			zero.append((i,j))
#print(*pan,sep='\n')
def check4(x,y,i):
	px=x//3*3
	py=y//3*3
	for h in range(3):
		for g in range(3):
			if i==pan[py+h][px+g]:
				return False
	return True
def checkx(y,i):
	for h in range(9):
		if i==pan[y][h]:
			return False
	return True
def checky(x,i):
	for h in range(9):
		if i==pan[h][x]:
			return False
	return True
def dfs(k):
	if k==len(zero):
		for i in range(9):
			print(*pan[i],sep = "")
		exit()
	for i in range(1,10):
		y=zero[k][0]
		x=zero[k][1]

		if check4(x,y,i) and checkx(y,i) and checky(x,i):
			pan[y][x]=i
			dfs(k+1)
			pan[y][x]=0
dfs(0)
print("Not Possible")
