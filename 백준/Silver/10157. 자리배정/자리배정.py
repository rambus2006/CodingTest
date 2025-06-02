C, R = map(int, input().split())
K = int(input())

if K > C * R:
    print(0)
    exit()

# 방향: 위, 오른쪽, 아래, 왼쪽 (문제 기준)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 방문 체크용 배열 (파이썬 인덱스는 0부터 시작, 좌석은 (1,1)부터)
# 실제로는 (x, y) 좌표계로 생각해도 무방
arr = [[False] * (C + 2) for _ in range(R + 2)]  # 테두리도 체크

# (1, 1)부터 시작 (파이썬 인덱스로는 (0,0)이지만, 문제 기준 (1,1)로 생각)
# 실제로는 (x, y) = (1, 1) ~ (C, R) 범위에서만 채움

x, y = 1, 1
dir = 0  # 시작 방향(위)
count = 1

while True:
    if count == K:
        print(x, y)
        break
    arr[y][x] = True  # 방문 체크
    # 다음 위치 계산
    nx = x + dx[dir]
    ny = y + dy[dir]
    # 다음 위치가 범위 밖이거나 이미 방문한 곳이면 방향 전환
    if nx < 1 or nx > C or ny < 1 or ny > R or arr[ny][nx]:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]
    x, y = nx, ny
    count += 1
