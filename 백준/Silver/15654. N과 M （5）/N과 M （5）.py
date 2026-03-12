from itertools import permutations

N,M = map(int,input().split())
Nlist = list(map(int, input().split()))

resultlist = list(permutations(Nlist,M))
resultlist.sort()
for r in resultlist:
    print(' '.join(map(str, r)))