import sys
def input():return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
c=[int(input()) for i in range(a)]
k=max(c)
for i in range(b-a):
    c.append(k)
c=list(map(str,c))

s=sorted([(int((i*11)[:11]),i) for i in c],reverse = True)
an = []
for i,j in s:
    an.append(j)
if an[0]=='0':
    print(0)
else:
    
    print("".join(an))
