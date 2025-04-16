import sys

cnt = 0
visited = [[0]*100 for _ in range(100)]
for tc in range(4):
    arr = list(map(int,sys.stdin.readline().split()))
    # x의 끝점
    square_x = abs(int(arr[0] - arr[2]))
    # y의 끝점
    square_y = abs(int(arr[1] - arr[3]))

    for squere_col in range(arr[1],(arr[1]+square_y)):
        for squere_row in range(arr[0],(arr[0]+square_x)):
            visited[squere_col][squere_row] = 1

for row in range(len(visited)):
    for col in range(len(visited)):
        if visited[row][col] == 1:
            cnt+=1
print(cnt)
