'''
[문제 분석]
> 문제 
- 자연수 M과 N이 주어질 때 M 이상 N 이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 
프로그램을 작성하시오. 
- 예를 들어  M = 60, N = 100인 경우 
60 <= x  <= 100 이하의 자연수 중 
소수는 
 61, 67, 71, 73, 79, 83, 89, 97
 이들 소수의 합은 620, 최솟값은 61이 된다. 

> 입력 
60
100

> 해결
- 0과 1은 소수가 아니다. 
- 2~num으로 나누어서 나머지가 0이 되는 값이 있으면 소수가 아니다.  
'''
m = int(input())
n = int(input())

decimalList = []
# n 이상~n 이하의 수 
for num in range(m,n+1): 
    # 만약 나눠지느 수가 있으면 카운트해서 값을 바꾼다. 
    count = 0
    # 2 이상의 수들 중에서 소수를 찾는다. 
    if num > 1:
        for i in range(2,num):
            if num % i == 0: 
              count += 1
              break
        if count == 0: 
            decimalList.append(num)

if len(decimalList) > 0: 
    print(sum(decimalList))
    print(min(decimalList))
else: 
    print(-1)
    

