for _ in range(int(input())):


    a = int(input())
    su=[]
    check = [0 for i in range(2*a-1)]
    for i in range(2*a-1):
            if i%2==0:
                    su.append(str(i//2+1))
            else:
                    su.append('')
    last=[]
    def dfs(k):#k는 1,3,5,7,...
            if k==2*a-1:
                    if eval(''.join(su))==0:
                            for j in range(2*a-1):
                                    if check[j]==1:
                                            su[j*2+1]=" "
                            
                            print(*su,sep='')
                            for j in range(2*a-1):
                                    if check[j]==1:
                                            su[j*2+1]=""
                    return
            for i in range(3):
                    if i==0:
                            su[k]=""
                            check[k//2]=1
                            dfs(k+2)
                            check[k//2]=0
                    elif i==1:
                            su[k]="+"
                            dfs(k+2)
                    else:
                            su[k]="-"
                            dfs(k+2)
    dfs(1)
    print()
                            
            
            
			