k = [int(input()) for i in range(10)]

j = set()
for i in k:
    j.add(i%42)
print(len(j))
    
