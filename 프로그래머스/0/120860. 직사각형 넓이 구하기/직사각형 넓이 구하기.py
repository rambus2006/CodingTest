def solution(dots):
    answer = 0
    #가로
    x = [dot[0] for dot in dots]
    #세로 
    y = [dot[1] for dot in dots]
    
    w = max(x) - min(x)
    h = max(y)-min(y)
    
    answer = w*h
    #직사각형의 넓이
    return answer