h,m = map(int,input().split())
if m >= 45: print(f"{h} {m-45}")
else:
    if h == 0:
        h = 24
    print(f"{h-1} {60+m-45}")