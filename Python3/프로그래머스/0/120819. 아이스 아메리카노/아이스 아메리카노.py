import math
def solution(money):
    answer = []
    cup=0
    mod =0
    #아니 뭐 아아에 미친 사람도 아니고...왜이렇게 비쌈? 
    # for i in range(0,money):
    cup = math.floor(money/5500)
    mod = int(money-cup*5500)
    
    answer.append(cup)
    answer.append(mod)
    return answer