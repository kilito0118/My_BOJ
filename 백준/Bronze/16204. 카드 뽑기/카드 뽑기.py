a,b,c=map(int,input().split())

k = [b,a-b,c,a-c]

print(min(k[0],k[2])+min(k[1],k[3]))
