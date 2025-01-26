def solution(array, n):
    box = []  # 각 요소와 n의 차이 절댓값을 저장할 리스트 초기화

    array.sort()  # array를 오름차순으로 정렬 (가장 작은 차이를 빠르게 찾기 위함)

    # array의 각 요소에 대해 n과의 차이 절댓값을 계산하여 box에 저장
    for i in array:
        box.append(abs(n - i))  # n과 i의 차이의 절댓값을 box에 추가

    # box에서 가장 작은 차이를 가진 요소의 인덱스를 찾아 그 값을 answer로 설정
    answer = [array[box.index(min(box))]]  # 최소 차이를 가진 값

    # 만약 차이가 같은 값들이 여러 개 있다면 그 중 더 작은 값을 선택
    if len(answer) > 1:
        return min(answer)  # 여러 개의 값이 있을 경우, 그 중 최소값을 반환
    else:
        return answer[0]  # 차이가 유일한 경우, 그 값을 반환
