a = int(input())
check = [[0 for i in range(a)] for i in range(a)]
cnt=0
def dfs(k):
	global cnt
	if k==a:
		cnt+=1
		#print(check)
		
		return
	for i in range(a):
		#왼쪽 위 대각, 오른쪽위 대각, 같은줄 조심
		if k==0:
			check[k][i]=1
			dfs(k+1)
			check[k][i]=0
			
		else:
			isri=1
			#왼대각 판별
			for j in range(a):
				if i-j>-1 and k-j>-1:
					if check[k-j][i-j]==1:
						
						isri=0
						break
				else:
					break
			if isri==0:
				continue
			#오른대각 판별
			for j in range(a):
				if i+j<a and k-j>-1:
					
					if check[k-j][i+j]==1:
						isri=0
						break
				else:
					break
			if isri==0:
				continue
			#같은줄 판별
			for j in range(k):
				if check[j][i]==1:
					isri=0
					break
				
			if isri==0:
				continue
			check[k][i]=1
			
			dfs(k+1)
			
			check[k][i]=0
			
			
				
			

dfs(0)
print(cnt)