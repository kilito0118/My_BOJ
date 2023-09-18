import sys
def input():return sys.stdin.readline().rstrip()
def dfs(k,h):
    global cnt
    if check[k]==1:
        return
    else:
        check[k]=1
        cnt+=1
        if h==0:
            for i in gra1[k]:
                dfs(i,0)
        else:
            for i in gra2[k]:
                dfs(i,1)
        
a,b,c = map(int,input().split())
gra1 = [[] for i in range(a+1)]
gra2 = [[] for i in range(a+1)]
check = [0 for i in range(a+1)]
for i in range(b):
    x,y=map(int,input().split())
    gra1[x].append(y)
    gra2[y].append(x)
cnt=0
dfs(c,1)
print(cnt,end=" ")
check[c]=0
cnt=0
dfs(c,0)
print(a-(cnt-1))
