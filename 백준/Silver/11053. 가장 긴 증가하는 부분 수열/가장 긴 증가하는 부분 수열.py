n = int(input())
s = list(map(int,input().split()))


dp =[1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if s[i]>s[j] and dp[i]<=dp[j]:
            dp[i] = dp[j] +1
print(max(dp))
