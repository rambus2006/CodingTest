from itertools import combinations

N,M = map(int,input().split())
dataset = [ i for i in range(1,N+1)]

permutation = sorted(list(combinations(dataset,M)))

for i in permutation:
    print(' '.join(map(str,i)))

