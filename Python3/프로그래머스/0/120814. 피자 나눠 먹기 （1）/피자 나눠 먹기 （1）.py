import math
def solution(n):
    answer = 0
    if(n<7):
        answer = 1
    for i in range(1,n):
        answer = int(math.ceil(n/7))
        
    
    return answer