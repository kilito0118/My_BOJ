#1167
import sys
def input():return sys.stdin.readline().rstrip()
a = int(input())
gra = [[] for i in range(a+1)]


for i in range(a):
    k = list(map(int,input().split()))
    cnt=0
    for j in k:
        if cnt==0:
            x = j
            cnt+=1
            continue
        elif cnt%2==1 and j!=-1:

            gra[x].append((k[cnt],k[cnt+1]))
        cnt+=1
    #시작점 받고     
d = 0
maxd = [0,0]
#print(gra)
check = [0 for i in range(a+1)]
def dfs(node):
    global d, maxd
    if check[node] == 1:
        return
    if d>maxd[0]:
        maxd[0]=d
        maxd[1] = node
    check[node] = 1
    for i,j in gra[node]:
        d+=j
        dfs(i)
        d-=j
    check[node] = 0

dfs(1)
gg = maxd[1]
maxd = [0,0]
dfs(gg)
print(maxd[0])

        
