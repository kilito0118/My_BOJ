import sys
def input(): return sys.stdin.readline().rstrip()
a = int(input())
b = [0 for i in range(1000002)]
for i in range(2,a+1):

    b[i] = b[i-1] +1
    if i%2==0:
        b[i] = min(b[i],b[i//2]+1)
    if i%3==0:
        b[i] = min(b[i],b[i//3]+1)


print(b[a])
k = b[a]
while True:
    print(a,end=" ")
    if b[a]==0:
        break
    if b[a-1]==k-1:
        a-=1
        k-=1
        
    elif a%3==0 and b[a//3]==k-1:
        a//=3
        k-=1
    elif a%2==0 and b[a//2]==k-1:
        a//=2
        k-=1
    
    
