num,M = map(int,input().split())
arr = list(map(int,input().split()))
max_sum = 0
for s in range(num):
    for i in range(s+1,num):
        for j in range(i+1,num):
            total = arr[s] + arr[i] + arr[j]
            if total <= M:
                max_sum = max(max_sum,total)

print(max_sum)