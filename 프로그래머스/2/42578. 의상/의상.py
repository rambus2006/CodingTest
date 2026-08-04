def solution(clothes):
    answer = 1
    dict = {}
    for c,j in clothes: 
        if j in dict: 
            dict[j] += 1
        else: 
            dict[j] = 1
    for i in dict.values():
        answer *= (1+i)
    
    return answer-1