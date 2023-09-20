import sys
def input():return sys.stdin.readline().rstrip()
a =[]
s = 0
an = []
c = 0
k=0
for i in range(int(input())):
    x=list(map(int,input().split()))
    
    if x[0]==1:
        s+=x[1]
        c+=1
        k^=x[1]
    elif x[0]==2:
        s-=x[1]
        c-=1
        k^=x[1]
    elif x[0]==3:
        an.append(str(s))
    else:
        an.append(str(k))
        
        
print("\n".join(an))
        
