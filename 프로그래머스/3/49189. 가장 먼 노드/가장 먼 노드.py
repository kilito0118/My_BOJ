from collections import deque

def solution(n, edge):
    check = [-1 for i in range(n+1)]
    zido = [[] for i in range(n+1)]
    for i,j in edge:
        zido[i].append(j)
        zido[j].append(i)
   #print(zido)
    q = deque()
    for i in zido[1]:
        q.append((1,i))
    while q:
        cnt,x = q.popleft()
        if check[x] == -1 or check[x]>cnt:
            check[x] = cnt
            for i in zido[x]:
                q.append((cnt+1,i))
    print(check)
    k = max(check)
    if k==-1:
        answer = 0
    else:
        answer = check[2:].count(k)
    return answer