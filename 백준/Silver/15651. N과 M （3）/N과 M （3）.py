from itertools import product

N,M = map(int,input().split())
dataset = [ i for i in range(1,N+1)]

permutation = product(dataset,repeat=M)

for i in permutation:
    print(' '.join(map(str,i)))

