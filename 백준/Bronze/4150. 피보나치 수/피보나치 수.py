a = int(input())
fi = [0 for i in range(10001)]
fi[0] = 0
fi[1] = 1
for i in range(2,10001):
    fi[i] = fi[i-1]+fi[i-2]
print(fi[a])