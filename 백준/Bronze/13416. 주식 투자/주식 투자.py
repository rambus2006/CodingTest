T = int(input())

for _ in range(T):
    N = int(input())
    total = 0

    for _ in range(N):
        A, B, C = map(int, input().split())
        total += max(A, B, C, 0)

    print(total)