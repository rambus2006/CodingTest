R, C, N = map(int, input().split())
grid = [list(input().strip()) for _ in range(R)]

# 2초에 전부 폭탄 채운 상태
allO = [['O'] * C for _ in range(R)]

# 3초에 폭탄 터뜨린 상태 만들기
boom1 = [['O'] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == 'O':
            boom1[i][j] = '.'  # 자기 자신 터짐
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < R and 0 <= nj < C:
                    boom1[ni][nj] = '.'

# 5초에 또 터짐 (boom1 기준으로)
boom2 = [['O'] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if boom1[i][j] == 'O':
            boom2[i][j] = '.'
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni = i + dx
                nj = j + dy
                if 0 <= ni < R and 0 <= nj < C:
                    boom2[ni][nj] = '.'

# 시간에 따라 어떤 결과 보여줄지 고름
if N == 1:
    for i in range(R):
        print(''.join(grid[i]))  # 그냥 입력 그대로 출력
elif N % 2 == 0:
    for i in range(R):
        print(''.join(allO[i]))  # 전부 O
elif (N - 3) % 4 == 0:
    for i in range(R):
        print(''.join(boom1[i]))  # 3초 상태 반복
else:
    for i in range(R):
        print(''.join(boom2[i]))  # 5초 상태 반복
