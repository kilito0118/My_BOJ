import sys
def input():return sys.stdin.readline().rstrip()

a,b=map(int,input().split())
c=list(input())
an=[c[0]]
cnt=1
for i in range(1,a):
    if b>0:
        while True: 
            if b==0 or cnt==0 or int(an[-1])>=int(c[i]):
                break
            b-=1
            an.pop()
            cnt-=1
    an.append(c[i])
    cnt+=1
        
if b>0:
    print("".join(an[:-b]))
else:
    print("".join(an))
