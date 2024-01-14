k = 0
last = 0
for i in range(5):
    a=sum(map(int,input().split()))
    if a>k:
        last = i+1
        k=a
print(last,k)