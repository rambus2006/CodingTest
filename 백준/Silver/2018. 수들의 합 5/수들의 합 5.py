n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1
while(end_index != n):  # 여기서 N -> n으로 수정
    if sum == n: 
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else: 
        end_index += 1
        sum += end_index
print(count)
