import sys
def input():return sys.stdin.readline().rstrip()
for i in range(int(input())):
    k = sorted(list(map(int,input().split())) for i in range(4))

    if (k[0][0]-k[1][0])**2+(k[0][1]-k[1][1])**2 == (k[0][0]-k[2][0])**2+(k[0][1]-k[2][1])**2 and ((k[0][0]-k[1][0])**2+(k[0][1]-k[1][1])**2)*2==(k[0][0]-k[3][0])**2+(k[0][1]-k[3][1])**2:
        print(1)
    else:
        print(0)
