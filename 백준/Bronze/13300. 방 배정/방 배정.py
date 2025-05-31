import math
students, room = map(int,input().split())

# 리스트 컴프리핸션으로 독립적인 배열을 만드는 실수를 했다.
arr = [[0]*7 for _ in range(2)]
cnt = 0
for _ in range(students):
    gen,age = map(int,input().split())
    arr[gen][age] += 1
for r in range(2):
    for c in range(1,7):
        cnt += math.ceil(arr[r][c]/room)

print(cnt)
