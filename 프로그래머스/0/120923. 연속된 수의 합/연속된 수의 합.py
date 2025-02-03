def solution(num, total): 
    temp = sum([i for i in range(1, num)])
    start = (total-temp) // num
    answer = [i for i in range(start,start+num)] 
    return answer