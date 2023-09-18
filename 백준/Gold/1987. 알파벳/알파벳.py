import sys
def input():return sys.stdin.readline().rstrip()
def dfs(x,y):
    global mcnt,cnt
    
    if x==a or y==b or x==-1 or y==-1 or alpha[ord(pan[x][y])-65]==1 or check[x][y]==1:
        mcnt=max(mcnt,cnt)
        if mcnt==26:
            print(26)
            exit()
        return
        
    else:
        alpha[ord(pan[x][y])-65]=1
        cnt+=1
        check[x][y]=1
        for i in range(4):
            
            dfs(x+dx[i],y+dy[i])
        check[x][y]=0
        cnt-=1
        alpha[ord(pan[x][y])-65]=0
        
    
    
alpha = [0 for i in range(26)]
a,b=map(int,input().split())
pan=[input() for i in range(a)]
check=[[0 for i in range(b)] for i in range(a)]
mcnt=0
cnt=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]
dfs(0,0)
print(mcnt)
