def solution(arr):
    answer = []
    minNum = min(arr)
    for item in arr:
        if item != minNum:
            answer.append(item)
    if answer == []:
        answer.append(-1)
    return answer