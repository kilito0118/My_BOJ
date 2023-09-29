import sys
def input():return sys.stdin.readline().rstrip()

a,b = map(int,input().split())

zido = [list(map(int,input().split())) for i in range(a)]
k = [[0 for i in range(a+1)] for i in range(a+1)]
sd = [0 for i in range(a+1)]
for i in range(a):
    for j in range(a):
        k[i][j] = zido[i][j]+k[i-1][j]
    sd[i] = sum(zido[i])

#print(*zido,sep='\n')
#print(*k,sep='\n')

for i in range(b):
    x,y,q,w = map(int,input().split())
    now = 0
    now+=sum(sd[x-1:q])

    for i in range(y-1):
        #print(now,(k[q-1][i] - k[x-2][i]))
        now -=(k[q-1][i] - k[x-2][i])
    #print(now)
    for i in range(w,a):
        
        now-=(k[q-1][i]-k[x-2][i])
    print(now)
    
