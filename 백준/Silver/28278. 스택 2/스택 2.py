'''
정수형 스택 구현,ㄴ
명령에 따라 처리하는 프로그램
1 : push(x)
2 : pop(x) 만약 스택 안에 아무것도 없는 경우 -1
3 : 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0 출력
5. 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없으면 -1출력

> 입력값을 받는다.
스택은 Last In, First Out (LIFO) 구조로,
마치 책 더미처럼 마지막에 넣은 게 가장 먼저 나오는 구조야.
✅ 기본 개념 정리
연산	설명
push(x)	스택에 x를 넣는다
pop()	스택에서 가장 위의 값을 꺼냄
top()	스택의 가장 위 값을 확인
empty()	스택이 비어있는지 확인
size()	스택에 들어있는 원소 개수
'''
import sys

n = int(sys.stdin.readline())
stack = []

for n in range(n):
    message = list(map(int,sys.stdin.readline().split()))

    if message[0] == 1:
        # 정수 x를 스택에 넣는다.
        stack.append(message[1])
    elif message[0] == 2:
        print(stack.pop() if stack else -1)
    elif message[0] == 3:
        print(len(stack))
    elif message[0] == 4:
        print(1 if not stack else 0)
    elif message[0] == 5:
        print(stack[-1] if stack else -1)
