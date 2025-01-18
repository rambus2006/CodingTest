def solution(balls, share):
    answer =0
    child = 1
    parent1=1
    parent2=1
    #분자 
    for n in range(balls,0,-1):
        child*=n 
    #분모m 팩토리얼 
    for m in range(share,0,-1):
        parent1 *= m
    #n-m 팩토리얼 
    for o in range((balls-share),0,-1):
        parent2 *= o
    
    #다 합치기 
    answer = child/(parent2*parent1)
    
    return answer
    