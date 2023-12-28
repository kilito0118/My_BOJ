a,b=map(int,input().split())
c,d=map(int,input().split())
if a>b:
    b,a=a,b
c=abs(c)
k = a%c
if d>=abs(c) or d<0:
    print("Unknwon Number")
    exit()

f = 0
last ="Unknwon Number"

for i in range(a//c,(b+c)//c+1):
    h = i*c+d
    if a<=h<=b:
        if f==0:
            last = h
            f=1
        else:
            print("Unknwon Number")
            exit()
else:
    print(last)
            
    