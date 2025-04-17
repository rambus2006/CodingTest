import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
result =[]
for idx in range(n):
    result.insert(arr[idx],idx+1)
print(*result[::-1])
