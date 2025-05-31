import sys
num = []
for _ in range(9):
    num.append(int(input()))


for i in range(0,9):
    for j in range(i+1,9):
        result = [num[k] for k in range(9) if k != i and k != j]
        if sum(result) == 100:
            result.sort()
            print(*result,sep="\n")
            sys.exit()
