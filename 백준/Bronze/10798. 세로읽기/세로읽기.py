'''
| 문제 분석 
> 구하라는 값
칠판에 붙어진 단어가 주어졌을 떄 영석이가 세로로 읽은 순서대로 글자들을 출력하는 프로그램을 작성하시오.  
> 출력값 
Aa0aPAf985Bz1EhCz2W3D1gkD6x
> 조건 
- 출력값에 줄바꿈 할 때 출력줄이 바뀌고 한줄로 쭉 출력되어야 한다.
- 글자는 A-Z,a-z,0-9까지 주어진다. 
> 입력값 
ABCDE
abcde
01234
FGHIJ
fghij

| 해결 방법
논리1)
(1) 2차원 배열로 받는다. map,list,input,for리스트 컴프리핸션 사용
(2) 세로로 5개씩 끊어 단어를 만들어 리스트에 저장한다. 
    90도 회전을 하여 끝에서부터 5개씩 끊어서 단어를 만든다. zip,map,list 함수 사용
(3) 리스트에 저장한 값을 순서대로 ''.join을 사용하여 출력한다. 
'''
arr = [list(input()) for _ in range(5)]
# 열 번호를 0부터 14까지 돌면서 
for col in range(15):
    # 각 행을 하나씩 읽는다. 
    for row in range(5):
        # 만약 열의 길이보다 행의 길이보다 큰 경우에만 출력 
        if col < len(arr[row]):
            print(arr[row][col],end='')

