import sys
def input():return sys.stdin.readline().rstrip()

a=int(input())
b=[list(map(int,input().split())) for i in range(a)]
su = 0
su1 = 0
for i in range(a-1):
    su+=b[i][0]*b[i+1][1]
su+=b[a-1][0]*b[0][1]
for i in range(1,a):
    su-=b[i][0]*b[i-1][1]
su-=b[0][0]*b[a-1][1]
print(abs(su/2))
