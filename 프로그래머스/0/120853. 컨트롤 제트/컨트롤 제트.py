def solution(s):
    answer = 0
    st = s.split(" ")
    stlen = len(st)
    for i in range(0,stlen) :
        # print(st[i])
        if(st[i]=="Z"):
            answer = answer - int(st[i-1])
        else: 
            answer+=int(st[i])

    return answer