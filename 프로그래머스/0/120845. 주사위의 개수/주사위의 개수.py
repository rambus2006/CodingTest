def solution(box, n):
    answer = 0
    
    arr = []
    #가로
    arr.append(box[0]//n)
    arr.append(box[1]//n)
    arr.append(box[2]//n)
    print(arr)
    answer = arr[0]*arr[1]*arr[2]
    return answer