def solution(s):
    answer = False
    pcnt = ycnt = 0
    for word in s:
        if word == "p" or word =="P":
            pcnt += 1
        if word == "y" or word == "Y":
            ycnt += 1
            
    if pcnt == ycnt:
        answer = True
    if pcnt == 0 and ycnt == 0:
        answer = True
    return answer
    