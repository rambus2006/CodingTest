import sys

for _ in range(4):
    ax,ay,ax2,ay2,bx,by,bx2,by2 = list(map(int,sys.stdin.readline().rstrip().split()))
    if ax2 < bx or bx2 < ax or ay2 < by or by2 < ay:
        print('d')
        continue
    elif (ax2 == bx or ax == bx2) and (ay2 == by or ay == by2):
        print('c')
        continue
    elif ax2 == bx or ax == bx2 or ay2 == by or ay == by2:
        print('b')
        continue
    else:
        print('a')
        continue
