import sys
def input():return sys.stdin.readline().rstrip()
a=int(input())
q=-1
m = dict()
cnt=0
for i in range(a):
    x,y=input().split()
    y=int(y)
    if y>1000:
        cnt+=1
        continue
    if q!=-1:
        if y>q:
            cnt+=1
            continue
    if y not in m:
        m[y]=1
    else:
        m[y]+=1
    if x=="jinju":
        q=y
m=sorted(m.items(),reverse=True)

for i,j in m:
    if i>q:
        cnt+=j
    else:
        break
print(q)
print(cnt)
