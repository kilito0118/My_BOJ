import sys
def input():return sys.stdin.readline().rstrip()
a=input()
ini=0
for i in a:
    if ini==0 and i=="U":
        ini+=1
  
    elif ini==1 and i=="C":
        ini+=1
       
    elif ini==2 and i=="P":
        ini+=1
        
    elif ini==3 and i=="C":
        ini+=1
        
        break
if ini==4:
    print("I love UCPC")
else:
    print("I hate UCPC")
