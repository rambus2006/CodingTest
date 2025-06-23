T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    res = ''
    R,S = map(str,input().split())
    S = list(S)
    R = int(R)
    for s in S:
        for i in range(R):
            res  += s
    print(res)