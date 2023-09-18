import sys
from collections import deque
def input(): return sys.stdin.readline().rstrip()

for i in range(int(input())):
    r = 0
    err = 1
    a = input()
    b = int(input())
    c = deque(input()[1:-1].split(","))
    if c[0] == "":
        c = deque()
    for i in range(len(a)):

        if a[i] == "R":
            r = r+1
        else:
            try:
                if r%2==0:
                    c.popleft()
                else:
                    c.pop()
            except:
                print("error")
                break
    else:
        if r%2==1 :
            gist = list(reversed(list(map(int,list(c)))))

        else:

            gist = list(map(int,list(c)))

            
        print("[",end = "")
            
        for i in range(len(gist)):
            if i != len(gist)-1:
                print("%d,"%gist[i],end="")
            else:
                print(gist[i],end ="")
        print("]")

