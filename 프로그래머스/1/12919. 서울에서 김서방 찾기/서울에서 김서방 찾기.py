def solution(seoul):
    for idx,word in enumerate(seoul):
        if "Kim" in word:
            x = idx
            break
    answer = "김서방은 " + str(x) + "에 있다"
    print(answer)
    return answer