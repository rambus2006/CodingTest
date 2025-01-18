def solution(rsp):
    answer = ''
    rspArr = list(rsp)
    rsplen = int(len(rspArr))
    print(rsplen)
    for i in range(0,rsplen):
        if rspArr[i] =='2':
            answer +='0'
        if rspArr[i] =='0':
            answer +='5'
        if rspArr[i] =='5':
            answer +='2'
    
    return answer