N,K = map(int,input().split())
coins = [ int(input()) for _ in range(0,N)]
coins.sort(reverse=True)
count = 0

for coin in coins:
    # 만약 K원보다 코인의 값이 작을 때
    if K >= coin:
        # K를 코인의 값으로 나눴을 때의 몫이 최솟값이 되어야 하는데 이부분을 놓쳤다.
        count += K // coin
        K = K % coin
print(count)