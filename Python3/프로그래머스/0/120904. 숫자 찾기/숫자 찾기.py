def solution(num, k):
    answer = 0
    numstr = str(num)
    
    # numlist = list(num)
    # numlength = len(numlist)
    answer = numstr.find(str(k))
    if(answer != -1):
        answer +=1
    return answer