import sys
def input():return sys.stdin.readline().rstrip()
sys.setrecursionlimit(2500)
def check(x,y):
    if dp[x][y]!=-1:
        return dp[x][y]
    elif x==y:
        return 1
    elif b[x]!=b[y]:
        dp[x][y] = 0
        return 0
    elif b[x]==b[y]:
        if x+1==y:
            return 1
        else:
            dp[x][y] = check(x+1,y-1)
            return dp[x][y]
    else:
        return 0
a = int(input())
b = list(map(int,input().split()))

dp = [[-1 for i in range(a)] for i in range(a)]
for i in range(a):
    dp[i][i] = 1

for i in range(int(input())):
    x,y = map(int,input().split())
    if dp[x-1][y-1]!=-1:
        print(dp[x-1][y-1])
    else:
        print(check(x-1,y-1))
