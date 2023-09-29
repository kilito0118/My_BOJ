import sys
def input():return sys.stdin.readline().rstrip()

a=int(input())
b = list(map(int,input().split()))
c = int(input())

k = max(b)
s = c//a
f=0
if sum(b)<=c:
    print(k)
    exit()


while True:
    su = 0
    for i in b:
        if s <i:
            su+= s
        else:
            su+=i
        if su>c:
            print(s-1)
            exit()

    s+=1
    
