a ,b = map(int,input().split())
s = sorted(list(map(int,input().split())))
maixmun = 0
for i in range(a):
    for j in range(i+1, a):
        for k in range(j+1, a):
            
            if b >= s[i]+s[j]+s[k] and maixmun< s[i]+s[j]+s[k]:
                    maixmun =  s[i]+s[j]+s[k]

print(maixmun)
