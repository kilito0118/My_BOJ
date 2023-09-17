import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())

b = list(map(int,input().split()))

cnt = 0
c = 0
for i in b:
    if i!=0:
        c+=1
        cnt=max(c,cnt)
    else:
        c = 0

print(cnt)
