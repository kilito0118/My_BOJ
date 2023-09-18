import sys
from queue import PriorityQueue

def input():return sys.stdin.readline().rstrip()
q = PriorityQueue()
a = int(input())
b = int(input())
check = [99999999999 for i in range(a+1)]

gra = [[] for i in range(a+1)]
for i in range(b):
    x,y,z = map(int,input().split())
    gra[x].append((z,y))
m,n = map(int,input().split())

for i in gra[m]:
    q.put(i)

while not(q.empty()):
    cnt,x = q.get()
    #print(x)
    if check[x] >cnt:
        check[x] = cnt
    else:
        continue
    
    for i,j in gra[x]:
        q.put((i+cnt,j))
print(check[n])