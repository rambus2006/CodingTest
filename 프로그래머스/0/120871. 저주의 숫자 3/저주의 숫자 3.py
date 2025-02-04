def solution(n):
    result = []
    num = 1
    
    while len(result) < n:
        if num % 3 != 0 and '3' not in str(num):  # 3의 배수나 숫자 3이 포함되지 않으면
            result.append(num)
        num += 1
    
    return result[n - 1]  # n번째 숫자를 반환

# 예시 테스트
print(solution(15))  # 25
print(solution(40))  # 76
