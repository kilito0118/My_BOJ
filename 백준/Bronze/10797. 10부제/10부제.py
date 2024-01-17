a=int(input())
b=list(map(int,input().split()))
cnt=0
for i in range(5):
    if b[i]%10==a:
        cnt+=1
print(cnt)