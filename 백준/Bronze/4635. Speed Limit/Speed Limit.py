import sys
def input():return sys.stdin.readline().rstrip()

while True:
    a=int(input())
    if a==-1:
        break
    last = 0
    dis = 0
    for i in range(a):
        x,y=map(int,input().split())
        dis+=x*(y-last)
        last = y
    print("{} miles".format(dis))
