n = int(input())
arr = list(map(int,input().split()))

# 연속구간이므로 1부터 시작 
dec = 1
aec = 1
max_dec = 1
max_aec = 1

for i in range(1,n):
    if arr[i-1] <= arr[i]:
        dec += 1
    else:
        dec = 1
    max_dec = max(dec, max_dec)

for i in range(1, n):
    if arr[i-1] >= arr[i]:
        aec += 1
    else:
        aec = 1
    max_aec = max(aec, max_aec)
    
print(max(max_aec,max_dec))