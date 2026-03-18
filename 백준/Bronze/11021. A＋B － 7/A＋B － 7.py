import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    a,b = list(map(int,sys.stdin.readline().split()))
    print(f"Case #{i+1}: {a + b}")