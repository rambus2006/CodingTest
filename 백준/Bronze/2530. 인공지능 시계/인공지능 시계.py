h,m,s = map(int,input().split())
cookingsecond = int(input())

totalsecond = h * 3600 + m * 60 + s + cookingsecond

second = totalsecond % 60
remainminute = totalsecond // 60
minute = remainminute % 60
hour = remainminute // 60

if hour >= 24:
    hour = hour % 24

print(f"{hour} {minute} {second}")
