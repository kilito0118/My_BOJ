import sys
def input():return sys.stdin.readline().rstrip()
def countnum(k):
    cnt = 0
    binum = bin(k)[2:]
    x = len(binum)
    for i in range(x):
        if binum[i]=="1":
            e = x-i-1
            cnt+=d[e]
            cnt+=(k-2**e+1)
            k=k-2**e
    return cnt



d = [0 for i in range(100)]


for i in range(1,70):
    d[i] = 2*d[i-1]+2**(i-1)
a,b=map(int,input().split())
print(countnum(b)-countnum(a-1))
