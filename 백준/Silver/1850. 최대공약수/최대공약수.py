import sys

def input(): return sys.stdin.readline().rstrip()
def chleorhddir(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
a,b = map(int,input().split())


print("1"*chleorhddir(a,b))
