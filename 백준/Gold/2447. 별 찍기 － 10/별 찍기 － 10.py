a = int(input())
stars = [[" " for i in range(a)] for i in range(a)]

def draw(scale,x,y):
	if scale>1:
		for i in range(x,x+scale,scale//3):
			for j in range(y,y+scale,scale//3):
				if i==scale//3+x and j==scale//3+y:
					continue
				draw(scale//3,i,j)
				#print(scale//3,i,j)
	else:
		stars[x][y]="*"
draw(a,0,0)
for i in stars:
	print("".join(i))

			
		