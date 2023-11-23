import sys

def input():return sys.stdin.readline().rstrip()


a,b=map(int,input().split())

zido=sorted([int(input()) for i in range(a)])
lp=0
rp=1

now=abs(zido[lp]-zido[rp])

m = 9999999999999999999999
while True:
    if lp>=a or rp>=a:
        break
    if lp==rp:
        rp+=1
        continue
    now=abs(zido[lp]-zido[rp])
    if now>=b:
        m = min(m,now)
        lp+=1
    else:
        rp+=1
print(m)
