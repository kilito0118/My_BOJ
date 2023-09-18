#11404
import sys

def input():return sys.stdin.readline().rstrip()
a = int(input())
gra = [[9999999999 for i in range(a)] for i in range(a)]
#print(*gra,sep = '\n')

for i in range(int(input())):
    x,y,z = map(int,input().split())
    x-=1
    y-=1
    gra[x][y] = min(z,gra[x][y])
    
for i in range(a):
    gra[i][i] = 0
for i in range(a):
    for j in range(a):
        for k in range(a):
            
            gra[j][k] = min(gra[j][k],gra[j][i]+gra[i][k])
for i in range(a):
    for j in range(a):
        if gra[i][j] == 9999999999:
            gra[i][j] = 0
for i in range(a):
    print(*gra[i],sep = " ")