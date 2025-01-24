def solution(my_string):
    # answer = []
    #문자열 안에 숫자만 반환 
    numbers = [int(num) for num in my_string if num.isdigit()]
    #숫자 오름차순으로 정렬 
    numbers.sort()
    
    return numbers