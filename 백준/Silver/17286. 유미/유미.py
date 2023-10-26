a,b=map(int,input().split())
people = [list(map(int,input().split())) for i in range(3)]




def line(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**(1/2)


k = line(a,b,people[0][0],people[0][1])+line(people[1][0],people[1][1],people[2][0],people[2][1])+min(line(people[0][0],people[0][1],people[1][0],people[1][1]),line(people[0][0],people[0][1],people[2][0],people[2][1]))
#첫 사람한테 가는 거리
k1 = line(a,b,people[1][0],people[1][1])+line(people[0][0],people[0][1],people[2][0],people[2][1])+min(line(people[0][0],people[0][1],people[1][0],people[1][1]),line(people[1][0],people[1][1],people[2][0],people[2][1]))
#두 번째
k2 = line(a,b,people[2][0],people[2][1])+line(people[1][0],people[1][1],people[0][0],people[0][1])+min(line(people[0][0],people[0][1],people[2][0],people[2][1]),line(people[1][0],people[1][1],people[2][0],people[2][1]))
print(int(min(k,k1,k2)))
