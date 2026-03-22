import sys

# 입력값 받기
n = int(sys.stdin.readline())

# 피보나치 수를 담을 리스트 (크기를 n+1만큼 0으로 초기화)
# n은 최대 45이므로 메모리 걱정은 안 하셔도 됩니다.
dp = [0] * (n + 1)

# n이 1 이상일 경우, 1번째 피보나치 수는 1로 설정
if n > 0:
    dp[1] = 1

# 2부터 n까지 반복하며 이전 두 개의 값을 더해서 채워 넣습니다.
for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]

# n번째 피보나치 수 출력
print(dp[n])