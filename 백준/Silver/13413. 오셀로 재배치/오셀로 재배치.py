T = int(input())

for _ in range(1,T+1):
    n = int(input())
    s = input()
    target = input()

    w = 0
    b = 0

    for i in range(n):
        if s[i] != target[i]:
            if s[i] == 'W':
                w += 1
            else:
                b += 1
    print(max(w,b))