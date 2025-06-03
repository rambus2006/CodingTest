N = int(input())
count = 0

if N >= 100:
    count += 99
    for num in range(110,N+1):
        num = str(num)
        if len(num) == 4:
            if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]) == int(num[2]) - int(num[3]):
                count += 1
        if len(num) == 3:
            if int(num[0]) - int(num[1]) == int(num[1]) - int(num[2]):
                count += 1
#100 미만의 수일 때 
else:
    for num in range(1,N+1):
        count += 1
print(count)