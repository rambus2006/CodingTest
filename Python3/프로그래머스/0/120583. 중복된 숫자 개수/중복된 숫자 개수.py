def solution(array, n):
    answer = 0
    arrlength = len(array)
    for i in range(0,arrlength):
        if(array[i]==n):
            answer+=1
    return answer