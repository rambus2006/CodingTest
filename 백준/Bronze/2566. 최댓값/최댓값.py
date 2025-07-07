N = 9
arr = [list(map(int,input().split())) for _ in range(N)]

maxValue = 0
resultrow = 0
resultcol = 0 
for row in range(N):
    for col in range(N):
        if arr[row][col] > maxValue:
            maxValue = arr[row][col]
            
for row in range(N):
    for col in range(N):
        if maxValue == arr[row][col]:
            resultrow = row + 1
            resultcol = col + 1

print(maxValue)
print(resultrow,resultcol)