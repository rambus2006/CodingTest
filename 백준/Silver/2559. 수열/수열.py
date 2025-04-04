N , K = list(map(int,input().split()))
daytmp = list(map(int,input().split()))
sumtmp = 0
max_tmp = 0

current = sum(daytmp[:K])
max_tmp = current

for i in range(1,N - K + 1):
    current = current - daytmp[i - 1] + daytmp[i + K - 1]
    if current > max_tmp:
        max_tmp = current
print(max_tmp)