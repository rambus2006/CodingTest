import math
def solution(my_str, n):
    answer = []
    li = list(my_str)
    sumstr =''
    length = math.ceil(len(li) / n)
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
        
    print(sumstr)
    return answer