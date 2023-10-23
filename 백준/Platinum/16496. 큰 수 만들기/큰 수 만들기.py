import sys
def input():return sys.stdin.readline().rstrip()
a=int(input())
b=input().split()
s=sorted([(int((i*11)[:11]),i) for i in b],reverse = True)
an = []
for i,j in s:
    an.append(j)
if an[0]=='0':
    print(0)
else:
    
    print("".join(an))
