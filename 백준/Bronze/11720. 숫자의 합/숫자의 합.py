a = int(input())
su = 0
b = int(input())
for i in range(a):
    su+=b%10
    b//=10
print(su)
