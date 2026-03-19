'''
1,2,3 중에서 중복없이 1개를 고른 수열을 만들어야 한다.
1,2,3,4 중에서 중복없이 2개를 고른 수열을 만들어야 한다.

def 함수 (원소)
    만약에 길이가 m개면
        print
        return
for num [1,2,3] 하면 num 에 1,2,3이 차례로 들어간다.
    함수 (원소 + num)
'''
import sys
n,m = map(int,sys.stdin.readline().split())

def func(path):
    if len(path) == m:
        print(*path)
        return
    for num in [i for i in range(1,n+1)]:
        if num in path: 
            continue
        func(path + [num])
func([])
