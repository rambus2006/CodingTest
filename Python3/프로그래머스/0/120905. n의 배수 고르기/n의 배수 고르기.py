def solution(n, numlist):
    answer = []
    i = 0
    listlength = len(numlist)
    for i in range(0,listlength):
        if numlist[i] % n == 0:
            answer.append(numlist[i])
    return answer