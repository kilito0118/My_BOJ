a,b = map(int,input().split())
c = sum(list(map(int,input().split())))
if c%b==0:
    print(1)
else:
    print(0)