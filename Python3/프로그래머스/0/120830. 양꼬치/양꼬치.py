def solution(n, k):
    answer = 0
    lambskewers=0;
    drink=0;
    lambskewers = n*12000
    drink = k*2000
    answer = lambskewers + drink
    
    
    divide = n//10
    answer-=2000*divide
    return answer