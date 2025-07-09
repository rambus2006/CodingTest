n = int(input())
room = 1
cnt = 1
while True:
    if n <= room:
        break
    room += 6 * cnt
    cnt +=1

print(cnt)