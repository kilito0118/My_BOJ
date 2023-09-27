import sys
def input():return sys.stdin.readline().rstrip()

def dfs(k,j):
    global su,cnt
    
    if su==b and j>0:
        cnt+=1
        
       
    
        
    for i in range(k,a):

        if check[i]==0:
            check[i] = 1
            su+=c[i]
            dfs(i,j+1)
            check[i] = 0
            su-=c[i]





a,b = map(int,input().split())
c = list(map(int,input().split()))
check = [0 for i in range(a)]
cnt = 0
su=0
dfs(0,0)
print(cnt)
