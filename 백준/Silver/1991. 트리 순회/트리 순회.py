from collections import deque
a= int(input())
dic = dict()


for i in range(a):
    z,x,y = input().split()
    dic[z] = [x,y]

def fir(x):
    if x!=".":
        print(x,end="")
        fir(dic[x][0])
        fir(dic[x][1])
def mid(x):
    if x!=".":
        mid(dic[x][0])
        print(x,end="")
        mid(dic[x][1])

def las(x):
    if x!=".":
        las(dic[x][0])
        
        las(dic[x][1])
        print(x,end="")
fir("A")
print()
mid("A")
print()
las("A")