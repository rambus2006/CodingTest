'''
문제 분석
> 구하고자 하는 값
수빈이가 동생을 찾을 수 있는 가장빠른 시간
> 입력값
- 첫번째 줄에 수빈이가 있는 위치 N과 K
> 출력
- 수빈이가 동생을 찾는 가장 빠른 시간
> 조건
- 0 < N < 100000여야 한다.
- 큐 써야 한다.
- 집가고싶다.
- BFS 써야 하네...
'''
from collections import deque

n,k = map(int,input().split())
queue = deque()

queue.append(n)
visited = [-1] * 100001
visited[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(visited[x])
        break
    for i in [x-1,x+1,x*2]:
        if 0 <= i <= 100000 and visited[i] == -1:
            visited[i] = visited[x] + 1
            queue.append(i)
