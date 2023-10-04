sosu = [0 for i in range(4000001)]

sosu[0] = 1
sosu[1] = 1
now = 0
for i in range(2,4000001):
    j = 2
    if sosu[i]==1:continue
    while i*j<4000001:

            sosu[i*j] = 1
            j+=1
    
sosuset = [0]
cnt = 0
for i in range(4000001):
    if sosu[i]==0:
        now+=i
        sosuset.append(now)
        cnt+=1
lp = 0
rp = 0
a = int(input())

cnt = 0
while True:
    if rp>283146:
        break
    k = sosuset[rp]-sosuset[lp]
    if k>a:
        lp+=1
    elif k<a:
        rp+=1
    else:
        cnt+=1
        rp+=1
print(cnt)
