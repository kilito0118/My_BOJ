a=int(input())
b=list(map(int,input().split()))
if a==1:
    b+=[0,0]
elif a==2:
    b+=[0]


cnt=27

dp = [[[27 for i in range(61)] for i in range(61)]for i in range(61)]


dp[b[0]][b[1]][b[2]] = 0

def fcount(x,y,z):
    global cnt
    if x<=0 and y<=0 and z<=0:
        cnt = min(cnt,dp[0][0][0])
        return
    for i in ((9, 3, 1), (9, 1, 3), (3, 1, 9), (3, 9, 1), (1, 9, 3), (1, 3, 9)):
        dx=0 if x-i[0]<0 else x-i[0]
        dy=0 if y-i[1]<0 else y-i[1]
        dz=0 if z-i[2]<0 else z-i[2]
        if dp[dx][dy][dz]>dp[x][y][z]+1:
            dp[dx][dy][dz] = dp[x][y][z]+1
            fcount(dx,dy,dz)
fcount(*b)
print(cnt)
        
