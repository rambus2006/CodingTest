a = int(input())
b = int(input())
c = int(input())

calc_result = a * b * c
calc_result = str(calc_result)

for n in range(10):
    print(calc_result.count(str(n)))