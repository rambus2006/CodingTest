N = int(input())
for _ in range(N):
    # A, B의 딱지 정보 입력 (맨 앞 개수는 버림)
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    # 4(별), 3(동그라미), 2(네모), 1(세모) 순서로 개수 비교
    for i in [4, 3, 2, 1]:
        cnt_a = a.count(i)
        cnt_b = b.count(i)
        if cnt_a > cnt_b:
            print("A")
            break
        elif cnt_b > cnt_a:
            print("B")
            break
    else:  # for문이 break 없이 끝나면 무승부
        print("D")
