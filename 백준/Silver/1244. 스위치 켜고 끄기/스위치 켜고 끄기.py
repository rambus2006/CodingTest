length = int(input())
switch = [0] + list(map(int,input().split()))
studentnum = int(input())

for i in range(studentnum):
    gen,switchidx = map(int,input().split())
    if gen == 1:
        cnt = 1
        while switchidx * cnt <= length:
            idx = switchidx * cnt
            switch[idx] = 1 - switch[idx]
            cnt += 1
    if gen == 2:
        left = right = switchidx
        while left > 1 and right < length and switch[left - 1] == switch[right + 1]:
            left -= 1
            right += 1
        for i in range(left,right + 1):
            switch[i] = 1 - switch[i]

for i in range(1,length + 1):
    print(switch[i],end=' ')
    if i % 20 == 0:
        print()