def solution(my_string, n):
    answer = ''
    arr = list(my_string)
    arrlength = len(arr)
    # print(arr)
    for i in range(0,arrlength):
        answer += arr[i]*n
        
    return answer