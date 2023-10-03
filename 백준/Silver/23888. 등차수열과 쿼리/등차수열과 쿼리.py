import math
import sys
def input(): return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
for i in range(int(input())):
    c,d,e = map(int,input().split())
    if c==1:
        
        f = a+(d-1)*b
        l = a+(e-1)*b
        if d==e:
            print(f)
            continue
        #print(f,l)
        print((e-d+1)*(f+l)//2)
    else:
        if d==e:
            print(a+(d-1)*b)
            continue
        print(math.gcd(a,b))
    
        
