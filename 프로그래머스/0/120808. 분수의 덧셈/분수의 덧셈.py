import math
def solution(numer1, denom1, numer2, denom2):
    answer = [0,0]
    if(denom1 == denom2):
        #분모가 같은 경우 -> 합
        answer[0] = numer1+numer2
        answer[1] = denom1
    else:
        #분모가 다른 경우
        lcm = denom1*denom2//math.gcd(denom1,denom2)
        
        numer1 *=(lcm//denom1)
        numer2 *=(lcm//denom2)
        
        #분자의 합
        answer[0] = numer1 +numer2
        answer[1]= lcm
    #기약 분수로 변환하기 
    gcd_value = math.gcd(answer[0],answer[1])
    answer[0] //= gcd_value
    answer[1] //= gcd_value
    
    
    return answer