for _ in range(3):  # 총 3번 윷놀이를 한다
    lst = list(map(int, input().split()))  # 한 줄씩 입력 받기
    total = sum(lst)  # 0이 1개 = 도(1), 0이 4개 = 모(0)
    
    if total == 3:
        print('A')  # 0이 1개
    elif total == 2:
        print('B')  # 0이 2개
    elif total == 1:
        print('C')  # 0이 3개
    elif total == 0:
        print('D')  # 0이 4개
    else:
        print('E')  # 0이 0개 → 모두 1 → 윷(4)
