count = 0

for i in range(8):
    row = input()
    for j in range(8):
        # 행과 열의 인덱스 합이 짝수이면 하얀칸
        if (i + j) % 2 == 0 and row[j] == 'F':
            count += 1

print(count)