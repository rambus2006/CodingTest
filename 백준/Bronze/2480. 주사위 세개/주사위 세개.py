'''
문제 링크: https://www.acmicpc.net/problem/2480

문제
- 1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은
규칙에 따라 상금을 받는 게임이 있다.
    1) 같은 눈이 3개가 나오면 10000원 + 같은 눈 * 1000원의 상금을 받게 된다.
    2) 같은 눈이 2개만 나오는 경우에는 1000원 + 같은 눈*100원의 상금을 받게 된다.
    3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.

'''
spot1,spot2,spot3 = map(int,input().split())


if spot1 == spot2 == spot3:
    prizemoney = 10000 + spot1 * 1000
else:
    if spot1 == spot2:
        prizemoney = 1000 + spot1 * 100
    elif spot2 == spot3:
        prizemoney = 1000 + spot2 * 100
    elif spot1 == spot3:
        prizemoney = 1000 + spot3 * 100
    else:
        # 모두 다 다른 경우
        prizemoney = max(spot1,spot2,spot3)*100

print(prizemoney)



