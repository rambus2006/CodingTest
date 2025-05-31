studentnum = int(input())
num = list(map(int,input().split()))
res = []
for s in range(studentnum):
    res.insert(len(res)-num[s],s+1)
print(*res)