import sys
def input(): return sys.stdin.readline().rstrip()

n,d,k,c=map(int,input().split())

rotatesusi=[int(input()) for i in range(n)]

x,y=0,0
susidict={}
meatsusi=0

while y<k:
    if rotatesusi[y] not in susidict.keys():
        susidict[rotatesusi[y]]=1
    else:
        susidict[rotatesusi[y]]+=1
    y+=1
if c not in susidict.keys():
    susidict[c]=1
else:
    susidict[c]+=1
while x<n:
    meatsusi=max(meatsusi,len(susidict))

    susidict[rotatesusi[x]]-=1
    if susidict[rotatesusi[x]]==0:
        del susidict[rotatesusi[x]]
    if rotatesusi[y%n] not in susidict.keys():
        susidict[rotatesusi[y%n]]=1
    else:
        susidict[rotatesusi[y%n]]+=1

    x+=1
    y+=1
print(meatsusi)
