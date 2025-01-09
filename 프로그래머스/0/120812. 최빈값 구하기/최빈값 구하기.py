def solution(array):
    answer = 0
    arr=[]
    count = {}
    for e in array:
        if e not in count :
            count[e] = 1
        else :
            count[e] += 1
    count = sorted(count.items(), key = lambda x : x[1], reverse = True)
    print(count)
    if len(count) > 1 and count[0][1] == count[1][1] :
        return -1
    else :
        return count[0][0]
