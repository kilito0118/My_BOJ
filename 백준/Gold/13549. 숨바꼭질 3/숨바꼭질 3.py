import sys
def input():return sys.stdin.readline().rstrip()



a,b = map(int,input().split())
wol = []
for i in range(200002):
    wol.append(abs(a-i))
for i in range(2*b):
    if i%2==0:
        wol[i] = min(wol[i//2],wol[i-1]+1,wol[i+1]+1,wol[i])
    else:
        wol[i] = min(wol[i-1]+1,wol[i+1]+1,wol[i],wol[i//2]+1,wol[i//2+1]+1)

print(wol[b])
