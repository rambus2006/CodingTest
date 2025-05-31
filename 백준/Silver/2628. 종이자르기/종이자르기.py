paperrow,papercol = map(int,input().split())
n = int(input())

width = [0,paperrow]
height = [0,papercol]

for _ in range(n):
    direct,line = map(int,input().split())
    # 세로로 자르는 것은 width, 가로로 자르는 것은 height라는 부분을 놓쳤다. 
    if direct == 0:
        height.append(line)
    if direct == 1:
        width.append(line)

width.sort()
height.sort()

max_w = max(abs(width[i-1] - width[i]) for i in range(1,len(width)))
max_h = max(abs(height[i-1] - height[i]) for i in range(1,len(height)))

print(max_w * max_h)