import sys
def input():return sys.stdin.readline().rstrip()
import heapq

#배열 만듬
#우선순위 큐로 관리
#한 점을 정하고 그 점에서 가장 작은거랑 연결
#만약 이미 연결된 거랑 연결하려고 하면 넘어감
#반복


def find(k):
    #print(k)
    if k==check[k]:
        return k
    check[k] = find(check[k])
    return check[k]
def union(x,y):
    x = find(x)
    y = find(y)
    if x<=y:
        check[x] = y
    else:
        check[y] = x
q = []
a,b = map(int,input().split())

for i in range(b):
    k = list(map(int,input().split()))
    k[2],k[0] = k[0],k[2]
    k = tuple(k)
    #print(k)
    heapq.heappush(q,k)
cnt = 0
check = [i for i in range(a+1)]
while q:
    value, x, y = heapq.heappop(q)
    x1 = find(x)
    y1 = find(y)
    if x1==y1:
        continue
    union(x,y)
    cnt+=value
   

print(cnt)

