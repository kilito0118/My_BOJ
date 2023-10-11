import sys
def input():return sys.stdin.readline().rstrip()
a = int(input())
if a==1:
    print(0)
    exit()
ta = list(map(int,input().split()))
an = [0 for i in range(a)]
temp = []
for i in range(a):
    while temp:
        
        if temp[-1][0]<ta[i]:
            x,y=temp.pop()
        else:
            x,y=temp[-1]
            an[i] = y+1
            break   
    temp.append((ta[i],i))
print(*an)    