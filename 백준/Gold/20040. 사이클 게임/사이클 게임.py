import sys
def input():return sys.stdin.readline().rstrip()
def set_find(k):
    if zido[k]==k:
        return k
    zido[k] = set_find(zido[k])
    return zido[k]
def set_union(q,w):
    q = set_find(q)
    w = set_find(w)
    if q>w:
        zido[q] = w
    else:
        zido[w] = q

a,b = map(int,input().split())
zido = [i for i in range(a)]
cnt = 0
for i in range(b):
    cnt+=1
    x,y = sorted(list(map(int,input().split())))
    if(set_find(x)==set_find(y)): break
    set_union(x,y)
else:
    print(0)
    exit()
print(cnt)
