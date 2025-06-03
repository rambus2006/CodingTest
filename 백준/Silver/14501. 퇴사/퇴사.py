N = int(input())
arr = []
for i in range(N):
    day,ben = map(int,input().split())
    arr.append((day,ben))

max_profit = 0
def solve(day,profit):
    global max_profit
    # 퇴사일에 도달하면 이익을 갱신하고 종료
    if day >= N:
        max_profit = max(max_profit,profit)
        return
    # 상담을 할 수 있으면
    if day + arr[day][0] <= N:
        # arr[day][0] : day 번째 날에 상담하는 데 걸리는 시간
        # arr[day][1] : day번째 날에 상담을 통해 얻을 수 있는 이익
        solve(day + arr[day][0],profit + arr[day][1])
    # 상담을 하지 않으면
    solve(day + 1,profit)
solve(0,0)
print(max_profit)