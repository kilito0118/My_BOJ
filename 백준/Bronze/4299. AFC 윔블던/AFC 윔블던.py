a,b=map(int,input().split())
x=(a+b)//2
y=(a-x)

if (a+b)%2==1 or a<0 or b<0 or a<b:
    print(-1)
else:
    print(x,y)
