import math
def solution(sides):
    answer = 0
    a,b = sorted(sides)
    answer= (a+b-1)-(abs(a-b))
    
    
    
    return answer