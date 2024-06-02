import sys
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
b = int(input())
plane = [int(input()) for i in range(b)]
visit = [i for i in range(a+1)]
cnt = 0
for i in plane:
    i = set_find(i)
    if i==0:
        break
    set_union(i-1,i)
    cnt+=1
    
print(cnt)
