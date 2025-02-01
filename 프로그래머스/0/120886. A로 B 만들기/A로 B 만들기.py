
def solution(before, after):
    answer = 0
    #리스트에 쪼개서 넣기
    #before 리스트의 값과 after값을 비교. 
    # if sorted(list(before))==sorted(list(after)):
    #     answer=1
    # else: 
    #     answer=0
    return 1 if sorted(list(before))==sorted(list(after)) else 0
    