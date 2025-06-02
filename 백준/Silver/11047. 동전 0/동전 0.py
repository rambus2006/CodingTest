n,k = map(int,input().split())
coins = [ int(input()) for k in range(n)]
coins.sort(reverse=True)
count = 0
for coin in coins:
    if k >= coin:
        count += k //coin
        k %= coin


print(count)