import sys
def input():return sys.stdin.readline().rstrip()

a=int(input())
b=input()


mcnt = 2001

for i in range(1,a):#주기
    c=list(b)
    cnt=0
    for x in range(a):
        if c[x] == "#":
            cnt+=1
            c[x] = "."
            
                
            for j in range(1,a):
                if j*i+x>=a:
                    break
                if c[j*i+x]==".":
                    #print(c)
                    break
                else:
                    c[j*i+x] = "."

    mcnt=min(mcnt,cnt)
    #print(cnt)
print(mcnt)
                
