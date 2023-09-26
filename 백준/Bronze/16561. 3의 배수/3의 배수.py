a=int(input())
cnt = 0
for i in range(1,1001):
    if i*3>=a: break
    for j in range(1,1001):
        if i*3+j*3>=a:
            break
        
        if (a-(i*3+j*3))%3==0:
            cnt+=1
            #print(a-(i*3+j*3))
            

print(cnt)
