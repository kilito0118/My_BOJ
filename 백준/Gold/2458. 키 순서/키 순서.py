#그래프 따라가면서 올라가거나 내려갈 때, 다 갈 수 있으면 알 수 있을것 같다.
import sys
def input():return sys.stdin.readline().rstrip()
def dfs(k,h):
    if check[k]==1:
        return
    else:
        check[k]=1
        if h==1:
            for i in gra1[k]:
                dfs(i,1)
        else:
            for i in gra2[k]:
                dfs(i,0)
a,b=map(int,input().split())
gra1 = [[] for i in range(a+1)]
gra2 = [[] for i in range(a+1)]
check = [0 for i in range(a+1)]
for i in range(b):
    x,y=map(int,input().split())
    gra1[x].append(y)
    gra2[y].append(x)
cnt=0
for i in range(1,a+1):
    check = [0 for _ in range(a+1)]
    
    dfs(i,1)
    check[i]=0
    dfs(i,0)
    for j in range(1,a+1):
        if check[j]==0:
            #print(i)
            break        
    else:
        cnt+=1
print(cnt)