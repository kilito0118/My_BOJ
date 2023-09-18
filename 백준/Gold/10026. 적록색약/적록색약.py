import sys
sys.setrecursionlimit(100000)
def input():return sys.stdin.readline().rstrip()
dx = [0,0,-1,1]
dy = [1,-1,0,0]
def dfs(x,y,c):

    if x==a or y==a or x==-1 or y==-1 or check[x][y] == 1:
        return
    if zido[x][y] in c:

        check[x][y] = 1
        
    else:
        return
    for i in range(4):
        dfs(x+dx[i],y+dy[i],c)
    


a = int(input())

zido = [list(input()) for i in range(a)]
check = [[0 for i in range(a)] for i in range(a)]
cnt = {"R":0, "G":0,"B":0}

for i in range(a):
    for j in range(a):
        if check[i][j] == 0:
            dfs(i,j,zido[i][j])
            cnt[zido[i][j]]+=1

print(sum(cnt.values()),end = " ")
check = [[0 for i in range(a)] for i in range(a)]
cnt = {"R":0,"B":0}
for i in range(a):
    for j in range(a):
        if check[i][j] == 0:
            if zido[i][j] == "G" or zido[i][j] == "R":
                dfs(i,j,("G","R"))
                cnt["R"]+=1
            else:
                dfs(i,j,"B")
                cnt[zido[i][j]]+=1
print(sum(cnt.values()))
