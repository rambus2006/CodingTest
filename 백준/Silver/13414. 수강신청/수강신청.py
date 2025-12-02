import sys
input = sys.stdin.readline

K, L = map(int, input().split())
mp = {}

for i in range(L):
    student = input().strip()
    mp[student] = i    # 마지막 클릭 순서로 덮어씀

# value(클릭 인덱스) 기준으로 정렬
sorted_list = sorted(mp.items(), key=lambda x: x[1])

# 앞에서 K명만 출력
for i in range(min(K, len(sorted_list))):
    print(sorted_list[i][0])
