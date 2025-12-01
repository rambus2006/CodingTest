T: int = int(input())
mp: dict[str, str] = {}

for _ in range(T):
    name, state = input().split()
    mp[name] = state

result: list[str] = sorted(
    [name for name, state in mp.items() if state == "enter"],
    reverse=True
)

for r in result:
    print(r)
