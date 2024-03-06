MD = 1000000007


def mat_mul(mat1,mat2,s1,s2):#행렬 곱하기
    mat = [[0 for i in range(s2[1])] for i in range(s1[0])]
    for i in range(s1[0]):
        for j in range(s2[1]):
            for k in range(s1[1]):
                mat[i][j]+=(mat1[i][k]*mat2[k][j])
                mat[i][j]%=MD
    return mat



def pow_re(mat,s1,n):
    if n==1 or n==0:
        return mat
    if n%2==0:
        nmat = pow_re(mat,[2,2],n//2)
        return mat_mul(nmat,nmat,[2,2],[2,2])
        
    else:
        nmat=pow_re(mat,[2,2],n-1)
        return mat_mul(nmat,mat,[2,2],[2,2])
        
        
        

for i in range(int(input())):
    a,b=list(sorted(map(int,input().split()),reverse = True))
    
    while True:
        if a%b==0:
            break
        a,b=b,a%b

    mat = [[1,1],
           [1,0]]
    #[[a,b],
    # [c,d]]
    #[[a*a+b*c,a*b+b*d],
    # [c*a+d*c,c*b+d*d]]




    print(pow_re(mat,[2,2],b)[0][1])
    

