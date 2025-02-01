def solution(i, j, k):
    answer = 0
    arr = [str(i_to_j) for i_to_j in range(i,j+1)]
    #한글자씩 자르기
    for i in range(0,len(arr)):
        for j in list(arr[i]):
            if j==str(k):
                answer+=1
    return answer