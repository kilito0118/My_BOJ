import sys
import bisect
def input():return sys.stdin.readline().rstrip()

a = int(input())
b=list(map(int,input().split()))

ans = [b[0]]
cnt = 1
for i in b:
    if ans[-1]<i:
        ans.append(i)
        cnt+=1
    else:
        ans[bisect.bisect_left(ans,i)] = i
    
print(cnt)
