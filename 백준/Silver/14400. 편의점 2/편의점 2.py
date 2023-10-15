import sys
def input():return sys.stdin.readline().rstrip()

a=int(input())
xpos=[]
ypos=[]

for i in range(a):
    x,y=map(int,input().split())
    xpos.append(x)
    ypos.append(y)
xpos.sort()
ypos.sort()
if a%2==0:
    k=(xpos[a//2]+xpos[a//2-1])//2
    j=(ypos[a//2]+ypos[a//2-1])//2
else:
    k=xpos[a//2]
    j=ypos[a//2]
an=0
for i in range(a):
    an+=abs(xpos[i]-k)+abs(ypos[i]-j)
print(an)
