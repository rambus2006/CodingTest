def solution(n):
    answer = 0
    nstr = str(n)
    nstrlength = len(nstr)
    arr=[]
    for i in nstr:
        arr.append(int(i))
    
    for j in range(0,nstrlength):
        answer+=arr[j]
    return answer