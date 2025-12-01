'''
문제링크: https://www.acmicpc.net/problem/7785
문제 분석
>구하라는 값
이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다. 로그가 주어졌을 때, 
현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.

> 조건
- 회사에는 동명이인이 없으며, 대소문자가 다른 경우에는 다른 이름이다. 사람들의 이름은 알파벳 대소문자로 구성된 5글자 이하의 문자열이다.
- 현재 회사에 있는 사람의 이름을 사전 순의 역순으로 한 줄에 한 명씩 출력한다.



> 입력값
로그에 기록된 출입 기록의 수 n이 주어진다. 
각 사람의 이름이 주어지고 "enter"나 "leave"가 주어진다. "enter"인 경우는 출근, "leave"인 경우는 퇴근이다.
4 
Baha enter
Askar enter
Baha leave
Artem enter

> 해결 논리
논리 1) 
딕셔너리로 저장 
dict = {"Baha":"상태",}

한줄씩
같은 이름인 겨우 상태 업데이트 하고 
새로운 이름인 경우 새로 추가 

set으로 상태가 enter인 것만 가져와서 저장 
사전순으로 역순으로 정렬 후 이름만 출력 
논리2)
set으로 상태가 enter 인 경우에만 set으로 저장. 만약 글
'''
# 논리1 = 런타임 에러 
T:int = int(input())
mp:dict[str,str] = {}
result:list[str] = []
# 한줄씩 입력 
for tc in range(1,T+1):
    # 타입 선언 
    name:str
    state:str

    # 새로운 이름인 경우 새로 추가 
    name,state = input().split()
    # 같은 이름인 경우 상태 업데이트 한다. 
    # 키가 같으니까 state 가 알아서 leave(마지막값)으로 바뀐다. 
    mp[name] = state

# result = [name for name,state in dict.items() if state == "enter"]
for name,state in mp.items():
    if state == 'enter':
        result.append(name)

result.sort(reverse=True)

for r in result: 
    print(r)