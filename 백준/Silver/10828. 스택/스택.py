import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    cmd = sys.stdin.readline().strip()

    if cmd.startswith('push'):
        _, value = cmd.split()
        stack.append(int(value))
    elif cmd == 'pop':
        print(stack.pop() if stack else -1)
    elif cmd == 'top':
        print(stack[-1] if stack else -1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if stack else 1)
