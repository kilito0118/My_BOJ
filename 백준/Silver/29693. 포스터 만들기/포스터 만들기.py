a,b = map(int,input().split())

zido = [list(input()) for i in range(a)]
#print(zido[1][b//2-1:b//2+2])
if b%2==0:
    for i in range(a):
        if zido[i][b//2-2:b//2+2] == ["X","X","X","X"] and b>=6:
            print("YES")
            for j in range(a):
                if i==j:
                    print("B"*((b-4)//2)+"W"+"Y"+"Y"+"W"+"B"*((b-4)//2))
                else:
                    print("B"*b)
            else:
                exit()
    else:
        print("NO")
        exit()
else:
    for i in range(a):
        #print(zido[i][b//2-1:b//2+2])
        #print(["X","X","X"])
        
        if zido[i][b//2-1:b//2+2] == ["X","X","X"] and b>=5:
            
            print("YES")
            for j in range(a):
                if i==j:
                    print("B"*((b-3)//2)+"W"+"Y"+"W"+"B"*((b-3)//2))
                else:
                    print("B"*b)
            else:
                exit()
    else:
        print("NO")
        exit()
            
