import sys

n = int(sys.stdin.readline())
score = [float(sys.stdin.readline().rstrip()) for i in range(n)]

score.sort(reverse=False)
for i in range(7):
    print(f"{score[i]:.3f}")
