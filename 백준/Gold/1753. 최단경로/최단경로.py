import sys
from queue import PriorityQueue

def input():return sys.stdin.readline().rstrip()
q = PriorityQueue()
a,b = map(int,input().split())
c = int(input())
check = [9999999999999 for i in range(a+1)]
check[c] = 0
gra = [[] for i in range(a+1)]
for i in range(b):
    x,y,z = map(int,input().split())
    gra[x].append((z,y))
for i in gra[c]:
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
for i in range(1,a+1):
    if check[i]==9999999999999:
        print("INF")
    else:
        print(check[i])


    
