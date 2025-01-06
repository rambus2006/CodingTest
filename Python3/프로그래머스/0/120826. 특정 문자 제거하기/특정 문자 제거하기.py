def solution(my_string, letter):
    answer = ''
    length = len(my_string)
    arr = [char for char in my_string]
    for i in range(0,length):
         if(arr[i] != letter):
            answer += arr[i]
    return answer