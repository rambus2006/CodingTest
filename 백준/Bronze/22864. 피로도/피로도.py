a,b,c,m = map(int,input().split())
hours = 24
work = 0
stress = 0
if a > m :
    print(0)
else:
    while hours > 0:
        if stress + a <= m:
            stress += a
            work += b
        else:
            stress = max(0,stress - c)
        hours -= 1
    print(work)