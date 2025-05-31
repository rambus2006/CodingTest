paper = [[0]*101 for _ in range(101)]
cnt = 0
for _ in range(4):
    ldx,ldy,rux,ruy = map(int,input().split())

    # 사각형 구해서 표시하기
    # 기존 값에서 더하는게 아니라 rux 좌표를 주기 때문에 그냥 거기까지 딱 하면 됟다
    for r in range(ldx,rux):
        for c in range(ldy,ruy):
            paper[c][r] = 1



for row in range(101):
    for col in range(101):
        if paper[row][col] >= 1:
            cnt += 1
print(cnt)