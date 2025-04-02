def convert_position(direction, distance, width, height):
    """(direction, distance)를 직사각형 경계의 1차원 좌표로 변환"""
    if direction == 1:  # 북쪽
        return distance
    elif direction == 2:  # 남쪽
        return width + height + (width - distance)
    elif direction == 3:  # 서쪽
        return 2 * (width + height) - distance
    elif direction == 4:  # 동쪽
        return width + distance

# 입력 받기
width, height = map(int, input().split())
num_stores = int(input())

# 상점들의 위치 저장
stores = []
for _ in range(num_stores):
    direction, distance = map(int, input().split())
    stores.append(convert_position(direction, distance, width, height))

# 동근이 위치 입력
donggeun_direction, donggeun_distance = map(int, input().split())
donggeun_pos = convert_position(donggeun_direction, donggeun_distance, width, height)

# 전체 둘레 길이
perimeter = 2 * (width + height)

# 최단 거리 계산
total_distance = 0
for store in stores:
    clockwise_dist = abs(donggeun_pos - store)  # 시계 방향 거리
    counterclockwise_dist = perimeter - clockwise_dist  # 반시계 방향 거리
    total_distance += min(clockwise_dist, counterclockwise_dist)

# 결과 출력
print(total_distance)
