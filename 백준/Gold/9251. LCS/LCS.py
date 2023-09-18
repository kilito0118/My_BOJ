a=input()
b=input()
x,y=len(a),len(b)
lcs = [[0 for i in range(y+1)] for i in range(x+1)]
for i in range(1,x+1):
	for j in range(1,y+1):
		if a[i-1]==b[j-1]:
			lcs[i][j]=lcs[i-1][j-1]+1
		else:
			lcs[i][j]=max(lcs[i-1][j],lcs[i][j-1])
print(lcs[x][y])
			
		