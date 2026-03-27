'''
문제링크: https://www.acmicpc.net/problem/10798
[문제 분석]
> 구하라는 값
칠판에 붙여진 단어들이 주어질 때, 영석이가 세로로 읽은 순서대로 글자들을 출력
> 조건
- 빈칸은 넘어가고 다음 문자를 이어서 읽는다.
> 입력
ABCDE
abcde
01234
FGHIJ
fghij
> 출력
Aa0FfBb1GgCc2HhDd3IiEe4Jj
> 해설
- 입력은 행기준으로 주어지는데, 세로 방향으로만 읽기만 하면 된다.
열 먼저 돌리고, 그다음 행으로 받는다.
- 0번째 열(col=0)일 때
A
a
0
F
f
- 1번째 열일 때(col=1)
B
b
1
G
g
그래서 이어 붙인다. 

'''
arr = [list(input()) for _ in range(5)]
# 가로(왼-> 오) 
for col in range(15):
    # 세로줄로 읽기 
    for row in range(5):
        # 각 줄의 길이가 다를 수 있기 때문에 5보다 작은 경우에만 넣게 하기 
        if col < len(arr[row]):
            print(arr[row][col],end='') # 뒤에 띄여쓰기 없게