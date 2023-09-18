import sys
def input():return sys.stdin.readline().rstrip()
a,b=map(int,input().split())
x = [int(input()) for i in range(a)]
arr=list(sorted(x))
l=1
r=1000000000
m=(l+r+1)//2
while l<r:
	cnt=1
	f=arr[0]
	for i in arr:
		if i-f>=m:
			cnt+=1
			f=i
	if cnt>=b:
		l=m
	else:
		r=m-1
	m=(l+r+1)//2
print(r)
		