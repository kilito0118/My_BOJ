import sys
import math
    

def input():return sys.stdin.readline().rstrip()

def set_find(k):
    if visit[k]==k:
        return k
    visit[k] = set_find(visit[k])
    return visit[k]
def set_union(q,w):
    q = set_find(q)
    w = set_find(w)
    if q>w:
        visit[q] = w
    else:
        visit[w] = q

a = int(input())
zido = [list(map(int,input().split()))+[i] for i in range(a)]
q = []
visit = [i for i in range(a+1)]
zido.sort(key = lambda x:x[0])
for i in range(a-1):
    q.append((abs(zido[i][0]-zido[i+1][0]),zido[i][-1],zido[i+1][-1]))
zido.sort(key = lambda x:x[1])
for i in range(a-1):
    q.append((abs(zido[i][1]-zido[i+1][1]),zido[i][-1],zido[i+1][-1]))

zido.sort(key = lambda x:x[2])
for i in range(a-1):
    q.append((abs(zido[i][2]-zido[i+1][2]),zido[i][-1],zido[i+1][-1]))

cnt = 0
q.sort()

for i in range((a-1)*3):
    dis,x,y = q[i]
    if(set_find(x)==set_find(y)):
        continue
    set_union(x,y)
    cnt+=dis
print(cnt)
