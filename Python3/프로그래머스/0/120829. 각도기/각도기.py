def solution(angle):
    answer = 0
    if(0<angle & angle<90):
        answer=1;
    elif(90 == angle):
        answer = 2;
    elif(90<angle & angle<180):
        answer = 3;
    else:
        answer = 4;
    return answer