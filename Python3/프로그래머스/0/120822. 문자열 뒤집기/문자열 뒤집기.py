def solution(my_string):
    answer = ''
    length = len(my_string)
    li=[]
    #문자열 리스트 만들기 
    li = list(my_string)
    for i in reversed(range(length)):
        answer = answer + li[i]

    return answer