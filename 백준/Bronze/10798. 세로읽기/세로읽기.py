'''
왼-> 오로 먼저 읽고, 세로로 5번 읽게 하는 것이 핵심.
왼-> 오로 먼저 읽을 때 최대 15개
이떄 길이가 5보다 작을 때만 이어 붙일 수 있게 허용해야 한다.
입력받을 때는 그대로
'''
board = [ str(input()) for _ in range(0,5)]
for col in range(0,15):
    for row in range(0,5):
        if col < len(board[row]):
            print(board[row][col],end='')