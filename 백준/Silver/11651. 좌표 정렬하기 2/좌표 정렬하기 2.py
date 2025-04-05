import sys

# 입력 받기
coord = []
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    x,y = sys.stdin.readline().rstrip().split()
    coord.append((int(x),int(y)))

coord.sort(key=lambda c:(c[1],c[0]))

for x,y in coord:
    print(x,y)