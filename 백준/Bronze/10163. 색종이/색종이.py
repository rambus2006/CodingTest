n = int(input())
paper = [[0]*1001 for _ in range(1001)]
for idx in range(1,n+1):
    x, y, w, h = map(int, input().split())

    for r in range(x,x+w):
        for c in range(y,y+h):
            paper[c][r] = idx

    # 2. 각 색종이별로 보이는 면적 세기
for idx in range(1, n + 1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if paper[i][j] == idx:
                cnt += 1
    print(cnt)
