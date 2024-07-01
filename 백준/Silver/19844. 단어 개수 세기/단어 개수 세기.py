import sys
def inptu():return sys.stdin.readline().rstrip()
a=input()
x = len(a)
fword = set(("c", "j", "n", "m", "t", "s", "l", "l", "d", "qu"))
mo = set(("a", "e", "i", "o", "u", "h"))
last = []
cnt = 1
for i in range(x):
    last.append(a[i])
    if a[i]==" " or a[i]=="-":
        cnt+=1
        last = []
    elif a[i]=="'":
        if "".join(last)[:-1] in fword and a[i+1] in mo:
            cnt+=1
            last = []
print(cnt)