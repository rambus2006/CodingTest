n = int(input())
L = [input().split() for _ in range(n)]
L.sort(key=lambda x: (int(x[3]),int(x[2]),int(x[1])))
Llen = len(L)

print(L[Llen-1][0])
print(L[0][0])
