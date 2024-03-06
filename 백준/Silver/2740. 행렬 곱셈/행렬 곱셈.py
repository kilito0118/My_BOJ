
def mat_mul(mat1,mat2,s1,s2):#행렬 곱하기
    mat = [[0 for i in range(s2[1])] for i in range(s1[0])]
    for i in range(s1[0]):
        for j in range(s2[1]):
            for k in range(s1[1]):
                #print(i,j,k)
                mat[i][j]+=mat1[i][k]*mat2[k][j]
                #print(i,j,k)
    return mat

s1=list(map(int,input().split()))
mat1=[list(map(int,input().split())) for i in range(s1[0])]
s2=list(map(int,input().split()))
mat2=[list(map(int,input().split())) for i in range(s2[0])]

#print(mat1,mat2)


result = mat_mul(mat1,mat2,s1,s2)
for i in range(s1[0]):
    print(*result[i],sep=" ")
        
