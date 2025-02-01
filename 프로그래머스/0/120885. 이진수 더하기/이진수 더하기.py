def solution(bin1, bin2):
    answer = ''
    arr = []
    
    # 두 이진수의 길이를 맞추기 위해 짧은 이진수에 0을 채워넣기
    max_len = max(len(bin1), len(bin2))
    bin1 = bin1.zfill(max_len)
    bin2 = bin2.zfill(max_len)
    
    # 올림 값 초기화
    carry = 0
    
    # 오른쪽부터 왼쪽까지 덧셈 수행
    for i in reversed(range(max_len)):
        # 각 자리의 값 더하기 (올림 값도 더함)
        total = int(bin1[i]) + int(bin2[i]) + carry
        
        if total < 2:
            arr.append(total)
            carry = 0
        elif total == 2:
            arr.append(0)
            carry = 1
        elif total == 3:
            arr.append(1)
            carry = 1
    
    # 마지막 올림값 처리 (carry가 1이면 1을 추가)
    if carry:
        arr.append(1)
    
    # arr을 뒤집어서 문자열로 반환
    arr.reverse()
    answer = ''.join(map(str, arr))
    
    return answer
