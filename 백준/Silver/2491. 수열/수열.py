import sys

arrlen = int(sys.stdin.readline().rstrip())
arr = list(map(int,sys.stdin.readline().split()))

rowarr = [1]*arrlen
colarr = [1]*arrlen
biggercnt = 1
for idx in range(arrlen-1):
    if idx + 1 < arrlen:
        if arr[idx] <= arr[idx+1]:
            rowarr[idx+1] += rowarr[idx]
        if arr[idx+1] <= arr[idx]:
            colarr[idx+1] += colarr[idx]
maxrow = max(rowarr)
maxcol = max(colarr)
result = max(maxrow,maxcol)
print(result)