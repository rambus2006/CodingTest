def solution(numbers, num1, num2):
    answer = []
    numlength = len(numbers)
    for i in range(num1,num2+1):
        answer.append(numbers[i])
    return answer