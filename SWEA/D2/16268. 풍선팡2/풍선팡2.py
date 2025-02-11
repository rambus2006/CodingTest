T = int(input())
for tc in range(1, T + 1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    res_max = 0
    for col in range(N):
        for row in range(M):
            sum_plus = matrix[col][row]
            for k in range(4):
                m_dx = row + dx[k]
                m_dy = col + dy[k]
                if 0 <= m_dx < M and 0 <= m_dy < N:
                    sum_plus += matrix[m_dy][m_dx]
            if res_max < sum_plus:
                res_max = sum_plus
    print(f"#{tc} {res_max}")