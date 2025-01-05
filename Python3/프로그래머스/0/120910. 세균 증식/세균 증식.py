def solution(n, t):
    answer = n
    sum =0;
    for i in range(1,t+1):
        answer = n*(2**i)
    
    return answer