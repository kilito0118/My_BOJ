a = int(input())
for i in range(a):
    print(" "*i+"*"*(a*2-1-2*i))
for i in range(a-2,-1,-1):
    print(" "*i+"*"*(a*2-1-2*i))
