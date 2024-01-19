a=[0 for i in range(26)]
for i in input():
    a[ord(i)-97]+=1
print(*a)