def solution(array, height):
    answer = 0
    arrlength = len(array)
    for i in range(0,arrlength):
        if(array[i]>height):
            answer+=1
    return answer