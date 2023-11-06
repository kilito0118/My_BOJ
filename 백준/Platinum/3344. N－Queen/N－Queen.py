from collections import deque

a = int(input())
lp = deque()
rp = deque()
for i in range(a):
    if (i+1)%2==0:
        lp.append(i+1)
    else:
        rp.append(i+1)
        
if a%6==2:
    for i in range(3):
        rp.popleft()
    rp.appendleft(1)
    rp.appendleft(3)
    rp.append(5)
elif a%6==3:
    lp.popleft()
    lp.append(2)
    rp.popleft()
    rp.popleft()
    rp.append(1)
    rp.append(3)
for i in lp:
    print(i)
for i in rp:
    print(i)
