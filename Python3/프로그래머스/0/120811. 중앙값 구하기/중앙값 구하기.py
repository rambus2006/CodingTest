def solution(array):
    answer = 0
    arrlength = len(array)
    array.sort()
    arrlength = arrlength //2
    answer = array[arrlength]

    return answer