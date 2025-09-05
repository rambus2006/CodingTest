'''
유형: 스택 구현
문제 분석
> 조건
- vps란
    - 괄호 기호 ( ) 가 기본형
    - 만약 x 가 vps 라면 이것을 하나의 괄호에 넣은 새로운 문자열 (x) 도 vps 가 된다.
    - 둘이 () 형태만 되면 ㅇㅋ
    - 짝이 안맞는 건 문자열
- 짝이 맞으면 YES,안맞으면 NO출력하는 문제

> 입력
6 # 테스트 케이스
(())()) # 스택에 넣을 것들
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(
> 출력
NO
NO
YES
NO
YES
NO
'''

T = int(input())

for i in range(1,T+1):
    stack = []
    vpsString = input()
    for i in vpsString:
        # 만약 여는 괄호('(') 였다면
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        # 만약 중간에 break로 탈출하지 않았다면 stack 짝이 다 맞는 것이다.
        if not stack:
            print("YES")
        else:
            print("NO")
