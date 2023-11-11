ball=[1,0,0]
for i in range(int(input())):
    a,b=map(int,input().split())
    ball[a-1],ball[b-1]=ball[b-1],ball[a-1]
print(ball.index(1)+1)
