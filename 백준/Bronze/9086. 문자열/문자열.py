T = int(input()) # test case 개수를 받아오는 코드
for tc in range(1, T+1):
    word = list(input())
    print(word[0]+word[len(word)-1])