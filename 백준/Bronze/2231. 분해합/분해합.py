a = int(input())
maker = 0
for i in range(1,a+1):
    maker = i
    for j in range(len(str(i))):

            
        
        maker = maker + int(str(i)[j])
      
    if(maker == a):
        print(i)
        exit()

else:
    print(0)
    exit()
    
