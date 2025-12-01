n = int(input())
present:set[str] = set()

for _ in range(n):
    name,action = input().split()

    if action == "enter": 
        present.add(name)
    else: 
        present.discard(name)
for name in sorted(present,reverse=True):
    print(name)