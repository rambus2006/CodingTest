# 입력받은 횟수
n = int(input())

# 스택 초기화
stack = []

# 수들을 처리
for _ in range(n):
    num = int(input())
    if num == 0:
        stack.pop()  # 가장 최근에 더한 수를 취소
    else:
        stack.append(num)  # 수를 스택에 추가

# 스택에 남은 값들의 합 출력
print(sum(stack))
