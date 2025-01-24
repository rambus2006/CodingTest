def solution(my_string):
    answer = 0
    # numbers = [int(num) for num in my_string if num.isdigit()]
    numbers = [int(num) for num in my_string if num.isdigit()]
    for i in numbers:
        answer+=i
    return answer