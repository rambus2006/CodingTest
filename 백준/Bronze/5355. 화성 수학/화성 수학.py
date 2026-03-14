'''
문제
겨울 방학에 달에 다녀온 상근이는 여름 방학 떄는 화성에 갔다 올 예정이다. 화성에서는 지구의
@ = *3
% = +5
# = -7
 수학 식의 가장 앞에 수가 하나 있고, 그 다음에는 연산자가 있다.

출력
3 테스트케이스개수 T
3 @ % 화성 수학식
10.4 # % @
8 #
'''
import sys

T = int(input())
for tc in range(1,T+1):
    inputlist = sys.stdin.readline().split()

    result = float(inputlist[0])

    oplist = inputlist[1:]
    for op in oplist:
        if op == '@':
            result *= 3
        elif op == '%':
            result += 5
        elif op == '#':
            result -= 7

    print(f"{result:.2f}")