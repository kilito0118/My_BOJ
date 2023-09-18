import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
c = sorted(list(map(int,input().split())))
d = sorted(list(map(int,input().split())))
la1 = c[0]
c1 = 1
c2 = 1
la2 = d[0]
for i in c:
    if la1+100<=i:
        la1 = i
        c1+=1
for i in d:
    if la2+360<=i:
        la2 = i
        c2+=1
print(c1,c2)