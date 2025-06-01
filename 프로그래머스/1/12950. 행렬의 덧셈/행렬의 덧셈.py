def solution(arr1, arr2):
    N = len(arr1)
    result = []
    for i in range(N):
        row = []
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
        result.append(row)
    return result