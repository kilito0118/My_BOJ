a=int(input())
for i in range(a):
    b = input()
    last = 0
    ans = 0
    for j in b:
        if j=="X":
            last = 0
        else:
            
            ans+=last+1
            last+=1
    print(ans)    
                
