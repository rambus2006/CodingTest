def solution(s):
    answer = 0
    if s[0] == '-':
        print(answer)
        answer = -int(s[1:])
        
    else:
        answer = int(s[0:])
    return answer