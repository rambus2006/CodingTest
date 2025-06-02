num = int(input())
time = []
for _ in range(num):
    start,end = map(int,input().split())
    time.append((start,end))

# 종료시간을 기준으로 오름차순 정렬
time.sort(key=lambda x:(x[1],x[0]))

#개수 저장
count = 0
end_time = 0
for start,end in time:
    if start >=end_time:
        count += 1
        end_time = end
print(count)