import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())
hu = [0 for i in range(a+1)]#진실을 알면 1아니면 0
reallist = list(map(int,input().split()))[1:]

for i in reallist:
    hu[i] = 1

party = sorted([sorted(list(map(int,input().split()[1:]))) for i in range(b)])
okparty = [0 for i in range(b)]

while True:
    w = hu.copy()
    for i in range(b):
        for j in party[i]:
            if hu[j]==1:
                okparty[i] = 1

    for i in range(b):
        if okparty[i]==1:
            for j in party[i]:
                hu[j]=1
        else:
            for j in party[i]:
                if hu[j]==1:
                    okparty[i]=1
        
    for i in range(b):
        if okparty[i]==1:
            for j in party[i]:
                hu[j]=1
        else:
            for j in party[i]:
                if hu[j]==1:
                    okparty[i]=1
    if w==hu:
        break
                
#print(hu)
print(okparty.count(0))
