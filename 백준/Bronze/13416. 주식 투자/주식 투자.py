T = int(input())
for tc in range(1,T+1):
    total = 0
    N = int(input())
    for n in range(0,N):
        li = [0,]
        li = li + list(map(int,input().split()))
        total += max(li)
    print(total)