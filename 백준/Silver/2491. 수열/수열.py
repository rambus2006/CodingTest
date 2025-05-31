n = int(input())
arr = list(map(int, input().split()))

# 증가(같거나 커지는) 구간
inc = 1
max_inc = 1
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        inc += 1
    else:
        inc = 1
    max_inc = max(max_inc, inc)

# 감소(같거나 작아지는) 구간
dec = 1
max_dec = 1
for i in range(1, n):
    if arr[i-1] >= arr[i]:
        dec += 1
    else:
        dec = 1
    max_dec = max(max_dec, dec)

print(max(max_inc, max_dec))