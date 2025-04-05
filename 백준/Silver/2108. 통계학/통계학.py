import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

# 산술 평균 (소수점 첫째 자리에서 반올림)
arithmean = round(sum(numbers) / n)

# 중앙값
numbers.sort()
median = numbers[n // 2]

# 최빈값
modearr = Counter(numbers).most_common()
max_freq = modearr[0][1]
candidates = [key for key, val in modearr if val == max_freq]
candidates.sort()
mode = candidates[1] if len(candidates) > 1 else candidates[0]

# 범위
scope = numbers[-1] - numbers[0]

print(f"{arithmean}\n{median}\n{mode}\n{scope}")
