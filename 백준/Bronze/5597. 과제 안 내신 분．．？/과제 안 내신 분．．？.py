arr = [0] * 30

for _ in range(28):
    num = int(input())
    arr[num - 1] += 1

for j in range(30):
    if arr[j] == 0:
        print(j + 1)