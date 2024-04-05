import sys
def input(): return sys.stdin.readline().rstrip()
a = [0 for i in range(10002)]
b = int(input())
for i in range(b):
    c = int(input())-1
    a[c] = a[c]+1

for k in range(10002):
    if(a[k] != 0):
        for j in range(a[k]):
            print(k+1)
    
