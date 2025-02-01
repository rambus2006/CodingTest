def solution(score):
    answer = []
    #avg=[(e + m)//2 for e,m in score]
    avg = [sum(i)/2 for i in score]
    sort_avg = sorted(avg, reverse=True) #내림차순
    #각 배열 별로 평균 값을 구한 리스트 만들기 
    for i in avg:
        answer.append(sort_avg.index(i)+1)
    #for i in avg:
     #   answer.append(sort_avg.index(i)+1)
        #print((score[i][j] + score[i][j+1])//2)
        # 등수 배정하기
    return answer