def solution(n):
    answer = 0
    arr = set()
    for i in range(1,n+1):
        if n%i == 0:
            arr.add(i)
    answer = sum(arr)
    return answer