for i in range(int(input())):
    a=input()
    if (int(a)+1)%int(a[-2:])==0:
        print("Good")
    else:
        print("Bye")
