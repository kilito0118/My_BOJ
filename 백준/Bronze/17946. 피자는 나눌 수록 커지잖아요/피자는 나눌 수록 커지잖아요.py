import sys
def input():return sys.stdin.readline().rstrip()
an = []
for i in range(int(input())):
    a = int(input())
    an.append(str((a**2+a+2)//2-((a+1)*a)//2))
print("\n".join(an))
