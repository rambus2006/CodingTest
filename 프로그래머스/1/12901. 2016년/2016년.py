import datetime
def solution(a, b):
    answer = ''
    day = datetime.date(2016, a,b)
    today = day.weekday()
    if today == 0:
        answer = "MON"
    if today == 1:
        answer = "TUE"
    if today == 2:
        answer = "WED"
    if today == 3:
        answer = "THU"
    if today == 4:
        answer = "FRI"
    if today == 5:
        answer = "SAT"
    if today == 6:
        answer = "SUN"
    return answer