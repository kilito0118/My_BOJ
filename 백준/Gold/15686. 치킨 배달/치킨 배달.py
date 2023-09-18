import sys
from itertools import combinations

def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
zido = [list(map(int,input().split())) for i in range(a)]

house = []
ch = []
cost = []

for i in range(a):
    for j in range(a):
        if zido[i][j] == 1:
            house.append((i,j))
        if zido[i][j] == 2:
            ch.append((i,j))
            cost.append(0)
            
r = 999999
for ii in combinations(ch,b):
    
    temp = 0
    
    for x,y in house:
        clen = 9999
        for h in range(b):
            
            clen=min(abs(ii[h][0]-x)+abs(ii[h][1]-y),clen)
        temp+=clen
    r = min(r,temp)

print(r)


