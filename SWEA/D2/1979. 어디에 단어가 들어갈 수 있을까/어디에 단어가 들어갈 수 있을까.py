'''
문제 분석
> 구하라는 값
특정 길이 K를 같는 단어가 들어갈 수 있는 자리의 수를 출력하는 프로그램을 작성하라
> 조건
가로/세로 모두 들어갈 수 있다.
N은 5이상 15이하의 정수 5<=N<=15
K 는 2 이상 N 이하의 정수  2<=K <=N
>입력값
테케
N,K
격자값
'''
def getword(grid,K):
    res = 0
    for line in grid:
        cnt = 0
        for word in line:
            if word == 1:
                cnt +=1
            else:
                # 0 을 만난다면
                if cnt >= 2 and cnt == K:
                    res += 1
                cnt = 0
        if cnt >= 2 and cnt == K:
            res += 1

    return res
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    row = getword(grid,K)
    grid90 = list(map(list,zip(*grid)))
    col = getword(grid90,K)
    print(f"#{tc} {row + col}")