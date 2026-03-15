import sys
N,M = map(int,input().split())

nlist = []
# ㅋㅋㅋㅋ듣도 못한 사람리스트
for n in range(0,N):
    nlist.append(sys.stdin.readline().rstrip())

mlist = []
# ㅋㅋㅋㅋㅋ보다못한 사람 리스트
for m in range(0,M):
    mlist.append(sys.stdin.readline().rstrip())

# 듣도 보도 못한 사람 리스트
result = sorted(list(set(nlist) & set(mlist)),reverse=False)
print(len(result))
print('\n'.join(map(str,result)))