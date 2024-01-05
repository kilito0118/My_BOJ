import sys
def input():return sys.stdin.readline().rstrip()

a=int(input())
q=[0 for i in range(a)]
w=[0 for i in range(a)]
e=[0 for i in range(a)]
r=[0 for i in range(a)]
for i in range(a):
    q[i],w[i],e[i],r[i] = map(int,input().split())
pa = dict()
for i in range(a):
    for j in range(a):
        if q[i]+w[j] in pa:
            pa[q[i]+w[j]] += 1
        else:
            pa[q[i]+w[j]] = 1
cnt=0
for i in range(a):
    for j in range(a):
        if -e[i]-r[j] in pa:
            cnt+=pa[-e[i]-r[j]]
print(cnt)

