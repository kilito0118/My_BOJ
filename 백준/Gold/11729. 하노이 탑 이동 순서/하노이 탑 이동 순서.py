a=int(input())
print(2**a-1)
def hano(n,start,end):
	if n==0:
		return
	m = 6-start-end
	hano(n-1,start,m)
	print(start,end)
	hano(n-1,m,end)
hano(a,1,3)