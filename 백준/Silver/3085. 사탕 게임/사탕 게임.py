N = int(input())
grid = [list(input()) for _ in range(N)]
answer = 0

def swap(x1, y1, x2, y2):
    grid[x1][y1], grid[x2][y2] = grid[x2][y2], grid[x1][y1]

def check():
    global answer
    for i in range(N):
        row_cnt = 1
        col_cnt = 1
        for j in range(1, N):
            # 행 체크
            if grid[i][j] == grid[i][j-1]:
                row_cnt += 1
            else:
                row_cnt = 1
            # 열 체크
            if grid[j][i] == grid[j-1][i]:
                col_cnt += 1
            else:
                col_cnt = 1
            answer = max(answer, row_cnt, col_cnt)

for i in range(N):
    for j in range(N - 1):  # j+1이 범위 넘어가지 않도록
        swap(i, j, i, j + 1)
        check()
        swap(i, j, i, j + 1)  # 원상복구

for j in range(N):
    for i in range(N - 1):  # i+1이 범위 넘어가지 않도록
        swap(i, j, i + 1, j)
        check()
        swap(i, j, i + 1, j)  # 원상복구

print(answer)