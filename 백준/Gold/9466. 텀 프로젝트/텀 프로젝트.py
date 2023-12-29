import sys
def input():return sys.stdin.readline().rstrip()

sys.setrecursionlimit(1000000)

def dfs(x):
    global cnt
    check[x]= 1
    cir.append(x)
    if check[c[x]]==1:
        if c[x] in cir:
            cnt-=len(cir[cir.index(c[x]):])
        return
    else:
        dfs(c[x])


a=int(input())
for i in range(a):
    b=int(input())
    
    c=[0]+list(map(int,input().split()))
    check=[0 for i in range(b+1)]
    cnt=b
    for j in range(1,b+1):
        if check[j]==0:
            cir=[]
            dfs(j)
    print(cnt)
