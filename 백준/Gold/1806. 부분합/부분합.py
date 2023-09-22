import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
c = list(map(int,input().split()))
nc = [0 for i in range(a+1)]
nc[1] = c[0]
for i in range(1,a):
    nc[i+1] = c[i]+nc[i]
x1 = 0
x2 = 0
k = 999999999999999999999999999# 길이
#print(nc)
while True:
    if x2==a+1 or x2==a+1:
        break
    #print(x1,x2)
    if x2==x1:
        x2+=1
        continue
    if nc[x2]-nc[x1]>=b:
        k = min(k,x2-x1)
        x1+=1
    elif nc[x2]-nc[x1]<b:
        x2+=1
if k==999999999999999999999999999:
    print(0)
else:
    print(k)
    
        
