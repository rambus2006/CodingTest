first_num = int(input())
max_len = 0
for second_num in range(1,first_num + 1):
    seq = [first_num,second_num]
    while True:
        next_num = seq[-2] - seq[-1]
        if next_num < 0:
            break
        
        # 음수를 포함하지 않느 문제 조건 
        seq.append(next_num)

    if len(seq) > max_len:
        max_len = len(seq)
        answer = seq
        # break를 하면 한번 계산하고 나가버림
print(max_len)
print(*answer)