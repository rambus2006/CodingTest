def solution(strlist):
    answer = []
    length = len(strlist)
    for i in range(0,length):
        answer.append(len(strlist[i]))
        
    return answer