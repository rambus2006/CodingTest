# 색종이 수
num = int(input())
paper = [[0] * 100 for _ in range(100)]

for i in range(num):
    W, D = map(int, input().split())
    for d in range(D,D+10):
        for w in range(W,W+10):
                paper[d][w] = 1

cnt = 0
for r in range(100):
    for c in range(100):
        if paper[r][c] >= 1:
            cnt += 1
print(cnt)