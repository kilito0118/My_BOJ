def solution(n, words):
    dic = {}
    answer = []
    last = words[0][0]
    turn = 1
    cnt = 0
   
    for i in words:
        
        
        if last!=i[0] or (i in dic):
            
            return [cnt+1,turn]
        dic[i] = 1
        last = i[-1]
        cnt+=1
        if(cnt==n):
            cnt=0
            turn+=1
    else:
        return [0,0]
    return answer