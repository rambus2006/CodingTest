def solution(emergency):
    # 응급도를 기준으로 내림차순으로 정렬된 배열
    sort_emergency = sorted(emergency, reverse=True)
    
    # 응급도의 순위를 딕셔너리로 저장
    emergency_rank = {value: rank + 1 for rank, value in enumerate(sort_emergency)}
    
    # 각 응급도의 순위를 정해서 반환
    answer = [emergency_rank[e] for e in emergency]
    
    return answer
