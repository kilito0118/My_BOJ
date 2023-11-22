import sys
def input():return sys.stdin.readline().rstrip()

a,b=map(int,input().split())
su=[list(map(int, input().split()[1:])) for i in range(a)]
lamp = [0 for i in range(b+1)]
lamp[0]=1
for i in su:
    for j in i:
        lamp[j]+=1

for i in su:
    flag=0
    for j in i:
        lamp[j]-=1
        if lamp[j]==0:
            flag=1
    if flag==1:
        for j in i:
            lamp[j]+=1
    else:
        print(1)
        break
else:
    print(0)
    
