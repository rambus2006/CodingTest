def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            sumnum = numbers[i] + numbers[j]
            answer.add(sumnum)
    return sorted(answer)
