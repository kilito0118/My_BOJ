import sys
def input():return sys.stdin.readline().rstrip()
dp=[0 for i in range(10001)]
dp[0]=1
dp[1]=1
for i in range(2,10001):
    dp[i]=dp[i-1]+dp[i-2]



for i in range(int(input())):
    a,b=map(int,input().split())
    print("Case #{0}: ".format(i+1),end="")
    print(dp[a-1]%b)
