from collections import deque
n,now,last,up,down=map(int,input().split())
q = deque()
q.append((now,0))

visit = set()
while q:
    
    k,f = q.popleft()
    
    if k==last:
        
        print(f)
        break
    if k>n or k<1 or k in visit:
        continue
    else:
        q.append((k+up,f+1))
        q.append((k-down,f+1))
        visit.add(k)
else:
    print("use the stairs")
