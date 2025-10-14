'''
[문제 분석]
- 배열 arr 이 주어질 때,(0~9까지 이루어져 있다.)
- 연속적으로 나타나는 숫자는 1쌍 빼고 다 삭제해야 한다. 
- 제거된 후 남은 수를 반환할 때 원소들의 순서를 유지해야 한다. 

> 조건 
> 입력값 
> 출력값
[해결 논리]
- i를 계속 이동해가면서 i+1 이 i 위치의 값과 같으면 한개만 남겨야 한다. 
- 왼쪽에서 오른쪽 방향으로 탐색해야한다. 

'''
def solution(arr):
    answer = []
    n = len(arr)
    for i in range(n):
        # 마지막 원소거나, 다음 원소와 다르면 append 
        if i == (n-1) or arr[i] != arr[i+1]:
            answer.append(arr[i])
    return answer