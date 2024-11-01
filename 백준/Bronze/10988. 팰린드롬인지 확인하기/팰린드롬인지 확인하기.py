def pel(st):
    try:
        if st[0]==st[-1]:
            return pel(st[1:-1])
        else:
            return 0
    except:
        return 1

a = input()
print(pel(a))
