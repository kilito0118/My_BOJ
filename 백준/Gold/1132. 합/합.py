import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

a = int(input())
nk=deque()
dic = {}
f = set()
for i in range(a):
    j = input()
    mm = len(j)
    
    f.add(j[0])
    for x in range(mm-1,-1,-1):
        if j[x] in dic:
            dic[j[x]]+= 10**(mm-x-1)
        else:
            dic[j[x]] = 10**(mm-x-1)

la = sorted(map(lambda x :(x[1], x[0]), dic.items()),reverse = True)

an = 0

if len(la)==10 and la[9][1] in f:
    for i in range(len(la)-1,-1,-1):
        if la[i][1] not in f:
            la[9],la[i] = la[i],la[9]
            break
    la.pop()
    la.sort(reverse=True)

for i in range(len(la)):
    an+=(9-i)*la[i][0]
#print(la)
print(an)

