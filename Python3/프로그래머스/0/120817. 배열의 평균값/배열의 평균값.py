def solution(numbers):
    answer = 0
    sum = 0
    numlength = len(numbers);
    
    for i in numbers:
        sum +=i 
    answer = sum / numlength
    return answer