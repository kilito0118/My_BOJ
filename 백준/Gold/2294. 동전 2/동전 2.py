import sys
def input():return sys.stdin.readline().rstrip()
a,b = map(int,input().split())
k = [int(input()) for i in range(a)]

coin = [10001 for i in range(10001)]
coin[0] = 0
for i in k:
    for j in range(i, b+1):
        
        
        coin[j] = min(coin[j],coin[j-i]+1)
        

print(-1 if coin[b]==10001 else coin[b])
#print(coin[b])
