E,S,M = map(int,input().split())

e = s = m = 0
count = 0
while True:
    e += 1
    s += 1
    m += 1
    if e > 15:
        e = 1
    if s > 28:
        s = 1
    if m > 19:
        m = 1
    count +=1
    if e == E and S == s and M == m:
        print(count)
        break