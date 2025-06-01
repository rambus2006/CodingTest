N = int(input())
info = []
array = [[-1] * 1001 for _ in range(1001)]

max_index_height, max_index_width = 0, 0  # 최대 인덱스를 저장할 변수 선언
for k in range(N):
    x1, y1, w, h = list(map(int, input().split()))  # 각각 x,y,넓이,높이 정보를 받는다.

    if max_index_height < y1 + h:  # 최대 행의 인덱스가 있다면.
        max_index_height = y1 + h  # 그 행을 최대행인덱스로 설정해준다.

    for a in range(y1, y1 + h):  # 높이 길이만큼돈다.
        array[a][x1:(x1 + w)] = [k] * w  # x1 ~ x1+w 까지의 배열을 모두 [k] * w 로 바꿔준다.

for k in range(N):  # N개수 만큼 돈다.
    count = 0  # 넓이를 저장할 변수 선언
    for i in range(max_index_height):  # 배열 길이만큼돈다.
        count += array[i].count(k)

    print(count)  # 해당 개수를 출력