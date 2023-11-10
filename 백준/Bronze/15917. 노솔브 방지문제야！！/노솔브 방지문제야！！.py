import sys
def input():return sys.stdin.readline().rstrip()
for i in range(int(input())):
    a=int(input())
    if (a&(-a)) == a:
        print(1)
    else:
        print(0)
