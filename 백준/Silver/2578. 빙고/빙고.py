'''
[문제 분석]
> 구하라는 값
사회자가 몇번째 수를 부른 후 철수가 빙고를 외치게 되는지 출력

> 조건
빙고판은 5*5 크기
수 범위는 1-25 까지

> 입력값
빙고판 (5줄)
사회자가 부르는 번호 순서(5줄)

--------------------------
> 해결 논리
- 사회자 순서를 순회하면서 해당 번호가 있으면 x 로 변경한다.
- x 로 변경할 때)
   - cnt += 1
   - x가 가로, 세로,대각선인지 순회한다. (True 면 멈춤) / False면 밖으로 )



> 실수한 부분
'''
def count_bingo(board):
    bingo = 0
    for row in board:
        if all(x == 0 for x in row):
            bingo += 1
    for col in range(5):
        if all(board[row][col] == 0 for row in range(5)):
            bingo += 1
    # 대각선 검사 (왼쪽 위 → 오른쪽 아래)
    if all(board[i][i] == 0 for i in range(5)):
        bingo += 1
    # 대각선 검사 (오른쪽 위 → 왼쪽 아래)
    if all(board[i][4-i] == 0 for i in range(5)):
        bingo += 1
    return bingo


bingogrid = [list(map(int,input().split())) for _ in range(5)]
calls = []
for _ in range(5):
    calls += list(map(int, input().split()))

for idx,num in enumerate(calls):
    for row in range(5):
        for col in range(5):
            if bingogrid[row][col] == num:
                bingogrid[row][col] = 0
    if count_bingo(bingogrid) >= 3:
        print(idx + 1)
        break


