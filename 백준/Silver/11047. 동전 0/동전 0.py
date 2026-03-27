N,K = map(int,input().split())
coins = [int(input()) for _ in range(0,N)]
coins.sort(reverse=True)
count = 0

for coin in coins:
    if K >= coin:
        count += K // coin
        K %= coin
print(count)
# 파이썬 싫어