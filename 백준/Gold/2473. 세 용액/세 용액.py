import sys
def input():return sys.stdin.readline().rstrip()
a = int(input())
b=sorted(map(int,input().split()))
#print(b)
an = [9999999999*3,b[0],b[1],b[2]]

for i in range(a-2):
    lp=i+1
    rp=a-1
    while True:
        if lp>=rp:
            break
        temp = b[lp]+b[rp]+b[i]
        x = abs(temp)
        if temp==0:
            an[0]=x
            an[1] = b[i]
            an[2]=b[lp]
            an[3]=b[rp]
            print(*an[1:])
            exit()
        elif temp>0:
            if an[0]>x:
                an[0]=x
                an[1] = b[i]
                an[2]=b[lp]
                an[3]=b[rp]
            rp-=1
        else:
            if an[0]>x:
                an[0]=x
                an[1] = b[i]
                an[2]=b[lp]
                an[3]=b[rp]
            lp+=1
            
print(*an[1:])
