import math

def solution(k, d):
    answer = 0
    max_i = d // k  # i의 최대값 계산
    d_squared = d * d
    
    for i in range(max_i + 1):
        i_k = i * k
        remaining = d_squared - i_k * i_k
        
        if remaining < 0:
            continue
        
        max_j_k = math.isqrt(remaining)  # j*k의 최대값
        j_max = max_j_k // k  # j의 최대값 계산
        answer += j_max + 1  # 0부터 j_max까지 카운트
        
    return answer