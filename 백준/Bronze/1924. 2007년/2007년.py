a,b = map(int,input().split())
c = ["SUN","MON","TUE","WED","THU","FRI",'SAT']
d = {0:0,1:31,3:31,5:31,7:31,8:31,10:31,12:31,4:30,6:30,9:30,11:30,2:28}
allday = b
for i in range(a):
    allday+=d[i]
print(c[allday%7])