import sys
def input():return sys.stdin.readline().rstrip()
a=int(input())
b=list(map(int,input().split()))
su=b[0]+b[-1]
nf=0
nl=a-1
msu=[b[0]+b[-1],0,a-1]

while True:
    if su==0:
        print(b[msu[1]],b[msu[2]])
        break
    elif su>0:
        nl-=1
        if nf>=nl:
            print(b[msu[1]],b[msu[2]])
            break
            
    else:
        nf+=1
        if nf>=nl:
            print(b[msu[1]],b[msu[2]])
            break
    
    su=b[nf]+b[nl]
    if abs(msu[0]) >abs(su):
        msu[0]=su
        msu[1]=nf
        msu[2]=nl
        

    
