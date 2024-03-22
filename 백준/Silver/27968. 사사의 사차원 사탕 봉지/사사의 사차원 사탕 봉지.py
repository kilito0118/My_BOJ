import sys
import bisect
def input(): return sys.stdin.readline().rstrip()
e = []
a,b = map(int,input().split())
c = list(map(int,input().split()))
d = [c[0]]
for i in range(1,b):
    d.append(d[-1]+c[i])

for i in range(a):
    k = int(input())
    if k>d[-1]:
        e.append("Go away!")
        
        continue

    e.append(str(bisect.bisect_left(d, k)+1))

    
print("\n".join(e))
