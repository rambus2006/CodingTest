'''
[문제 분석]
> 문제에서 구하라는 값
입력으로 종이의 가로,세로 길이 그리고 잘라야할 점선들이 주어질 때
가장 큰 종이조각의 넓이(cm)

> 조건
- 가로세로의 최대길이는 100cm

> 입력
10 8 //종이의 가로 / 종이의 세로
3 // 칼로 잘라야 하는 점선의 개수
//점선(가로는 0 세로는 1) 점선번호호0 3 //점선 1
1 4
0 2
'''
paperrow ,papercol = map(int,input().split())
cuts = int(input())

width = [0,paperrow]
height = [0,papercol]

for c in range(cuts):
    cutdir,linenum = map(int,input().split())
    if cutdir == 0:
        height.append(linenum)
    else:
        width.append(linenum)

width.sort()
height.sort()

max_w = max(width[i+1] - width[i] for i in range(len(width)-1))
max_h = max(height[i+1] - height[i] for i in range(len(height)-1))

print(max_w*max_h)
