a={'136':1000,'142':5000,'148':10000,'154':50000}
cnt=0
for i in range(int(input())):
    cnt+=a[input().split()[0]]
print(cnt)
