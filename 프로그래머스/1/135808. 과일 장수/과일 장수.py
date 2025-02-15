def solution(k, m, score):
    #print([0,1,2,3][-2])
    a = 0
    answer = 0
    x =sorted(score,reverse = True)
    for i in x:
        a+=1
        if(a==m):
            a=0
            answer+=m*i
            
    
    return answer