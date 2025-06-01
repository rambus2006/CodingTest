# def solution(n):
#     answer = 0
#     for x in range(1,n):
#         if x**2 == n:
#             answer = (x+1)**2
#             break
#         else: 
#             answer = -1
#     return answer
import math

def solution(n):
    x = math.isqrt(n)
    if x * x == n:
        return (x + 1) ** 2
    else:
        return -1
