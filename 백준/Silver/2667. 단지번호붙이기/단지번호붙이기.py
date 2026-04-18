'''
문제 정리
구하고자 하는 값 : 단지수, 각 단지에 속하는 집의 수(오름차순)

- 대각선은 연결 안됨
입력값
7 # 지도의 크기 N (가로 세로 같음)
0110100 #
0110101
1110101
0000111
0100000
0111110
0111000

출력
3 # 총 단지 수
7 # 단지내의 수 중 낮은 거 -> 높은 거 (오름차순 = sort한번)
8
9
해결방법
- dfs,bfs 둘 다 사용 가능하다
- rstrip 쓰기
-
'''
import sys

# 담을 배열 및 변수 선언
# 지도 배열
graph = []
# 단지 수
result = []
# 입력받기(readline사용)
input = sys.stdin.readline
n = int(input())

# 지도 담기
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

# dfs 만들기
dx = [0,0,-1,1]
dy = [1,-1,0,0]
count = 0

def dfs(i,j):
    global count
    # i 와 j 가 범위 내의 값인지
    if i < 0 or i >= n or j < 0 or j >= n:
        return
    # ij 값이 1일 때
    if graph[i][j] == 1:
        count += 1
        graph[i][j] = 0

        for idx in range(4):
            nx = i + dx[idx]
            ny = j + dy[idx]
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i,j)
            result.append(count)
            count = 0
result.sort()
print(len(result))
for li in result:
    print(li)