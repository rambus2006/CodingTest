# 전역변수 선언
n = int(input())
count = 0
move = []

# 함수 선언
def hanoi(n,start,end):
    global count
    if n:
        hanoi(n-1,start,6-start-end)
        move.append((start,end))
        count += 1
        hanoi(n-1,6-start-end,end)

# 호춯
hanoi(n,1,3)
print(count)
for start,end in move:
    print(start,end)
