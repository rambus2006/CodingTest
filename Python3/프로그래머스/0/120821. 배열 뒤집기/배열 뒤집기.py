def solution(num_list):
    answer = []
    list_length = len(num_list)
    for i in reversed(range(0,list_length)):
        answer.append(num_list[i])
    return answer