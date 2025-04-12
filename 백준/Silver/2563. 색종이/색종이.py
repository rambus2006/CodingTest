'''
100 * 100 의 배열을 만든다.
위치들을 받아온다. (3,7)...
---> 이부분 반복
3(x값은 그대로),7은 + 10 = 17 부터 10칸,* 아래로 10칸
해서 visited로 바꿔준다.
---> 방문한 곳(1인 부분)이 있으면
 +=1을 해주고 출력한다.
'''
import sys

grid = [[0]*100 for _ in range(100)]
loc = []
aplus = 0
cnt = 0
bplus=0
n = int(sys.stdin.readline())
for _ in range(n):

    a,b = list(map(int, input().split()))

    for row in range(a,a+10):
        for col in range(b,b+10):
            if grid[row][col] == 0 and 0<=grid[row][col] < 100:
                grid[row][col] = 1

for i in grid:
    cnt += i.count(1)

print(cnt)
