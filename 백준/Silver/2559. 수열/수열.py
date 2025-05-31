N,K = map(int,input().split())
arr = list(map(int,input().split()))

window_sum = sum(arr[:K])
max_sum = window_sum

for i in range(K,N):
    window_sum = window_sum - arr[i-K] + arr[i]
    max_sum = max(max_sum,window_sum)
print(max_sum)
