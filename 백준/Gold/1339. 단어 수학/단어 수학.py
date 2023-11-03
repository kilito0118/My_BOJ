import sys
from collections import deque
def input():return sys.stdin.readline().rstrip()

a = int(input())
nk=deque()
dic = {}

for i in range(a):
    j = input()
    mm = len(j)
    for x in range(mm-1,-1,-1):
        if j[x] in dic:
            dic[j[x]]+= 10**(mm-x-1)
        else:
            dic[j[x]] = 10**(mm-x-1)

la = sorted(dic.values(),reverse = True)
an = 0
#print(la)
for i in range(len(la)):
    an+=(9-i)*la[i]
print(an)

