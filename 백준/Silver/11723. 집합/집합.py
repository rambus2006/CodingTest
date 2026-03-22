import sys

T = int(sys.stdin.readline())
zero = set()

for tc in range(1,T+1):
    calc = sys.stdin.readline().split()
    if calc[0] == 'add':
        zero.add(int(calc[1]))
    elif calc[0] == 'remove':
        zero.discard(int(calc[1]))
    elif calc[0] == 'check':
        x = (int(calc[1]))
        if x in zero:
            print(1)
        else:
            print(0)
    elif calc[0] == 'toggle':
        x = int(calc[1])
        if x in zero:
            zero.remove(x)
        else:
            zero.add(x)
    elif calc[0] == 'all':
        zero = {t for t in range(1,21)}
    elif calc[0] == 'empty':
        zero = set()
    else:
        print('Error')
