def solution(price):
    answer = 0
    '''
    10만원 이상 5%
    30만원 이상 10%
    50만원 이상 20%
    '''
    if(price>=500000):
        answer = price * 0.8
    elif(price>=300000 and price<500000):
        answer = price * 0.9
    elif(price>=100000 and price<300000):
        answer = price * 0.95
    else: 
        answer = price
    answer = int(answer)
    
    return answer