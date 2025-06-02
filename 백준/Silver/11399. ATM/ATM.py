peoplenum = int(input())
people = []
time = list(map(int,input().split()))
timedict = dict()
for md in range(peoplenum):
    timedict[md+1] = time[md]

timedictkeys = sorted(timedict,key=timedict.get)
res = 0
cnt = 0

for i in range(peoplenum):
    cnt += timedict[timedictkeys[i]]
    res += cnt

print(res)