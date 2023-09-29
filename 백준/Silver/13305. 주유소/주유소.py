import sys
def input():return sys.stdin.readline().rstrip()
a = int(input())
b = list(map(int,input().split()))
c = list(map(int,input().split()))

now = 0
last = 99999999999

for i in range(a-1):
    if last>c[i]:
        last = c[i]
        
    
    now+=last*b[i]
print(now)
