def solution(order):
    answer = 0
    od = list(str(order))
    for i in range(0,len(od)):
        if int(od[i])==3 or int(od[i])==6 or int(od[i])==9:
            answer+=1
    return answer