import sys
def input():return sys.stdin.readline().rstrip()

a = int(input())
b = input().split()

f = [-1 for i in range(a*2+1)]
for i in range(a):
    f[i*2+1]=b[i]

check = [0 for i in range(10)]

last = []

def dfs1(k):
    
    if k==2*a+2:
        last.append("".join(f[::2]))
        for i in range(10):
            check[i] = 0
        for i in range(9,-1,-1):
            check[i] = 1
            f[0] = str(i)
            dfs2(2)
            check[i] = 0
    
    for i in range(10):
        if check[i] == 0:
            check[i] = 1
            f[k] = str(i)
            #print(f)
            if eval("".join(f[:k+1])):
                dfs1(k+2)
                check[i] = 0
                
            else:
                check[i] = 0

def dfs2(k):
    
    if k==2*a+2:
        print("".join(f[::2]))
        print(*last)
        exit()
    
    for i in range(9,-1,-1):
        if check[i] == 0:
            check[i] = 1
            f[k] = str(i)
            #print(f)
            if eval("".join(f[:k+1])):
                dfs2(k+2)
                check[i] = 0
                
            else:
                check[i] = 0

for i in range(10):
    check[i] = 1
    f[0] = str(i)
    dfs1(2)
    
    check[i] = 0
