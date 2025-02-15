from collections import deque
def solution(n, wires):
    zido = [[] for i in range(n+1)]
    count = [0 for i in range(n+1)]
    mcnt = 200
    for i,j in wires:
        zido[i].append(j)
        zido[j].append(i)
        count[i]+=1
        count[j]+=1
    answer = -1
    print(zido)
    for i in range(1,n+1):#어디서 자를지
        x = len(zido[i])
        
        if x<2:
            continue
        #print(zido[i])
        for j in range(x):#어떤걸 자를지
            q = deque()
            for k in range(x):#자른거 빼고 넣기
                if(k==j):
                    continue
                q.append(zido[i][k])
            check = [-1 for i in range(n+1)]
            check[i] = 1
            cnt = 1
            print(check)
            while q:
                y = q.popleft()
                if check[y] == 1:
                    continue
                check[y] = 1
                cnt+=1
                #print(y)
                for ne in zido[y]:
                    q.append(ne)
            print(cnt)
            mcnt = min(abs(n-cnt-cnt),mcnt)
    return mcnt