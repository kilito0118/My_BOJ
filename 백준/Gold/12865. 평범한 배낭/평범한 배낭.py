import sys
def input():return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
w=[]
v=[]
dp = [[0 for i in range(b+1)] for i in range(a+1)]
for i in range(a):
	x,y=map(int,input().split())
	w.append(x)
	v.append(y)
for i in range(1,a+1):
	for j in range(1,b+1):
		dp[i][j]=dp[i-1][j]
		if w[i-1]<=j:
			dp[i][j]=max(dp[i][j],dp[i-1][j-w[i-1]]+v[i-1])
print(dp[a][b])