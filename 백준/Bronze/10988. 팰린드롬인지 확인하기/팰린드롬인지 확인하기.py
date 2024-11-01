def pel(st,n):
    if(n<2):
        return 1
    if st[0]==st[-1]:
        return pel(st[1:-1],n-2)
    else:
        return 0



a = input()
print(pel(a,len(a)))
