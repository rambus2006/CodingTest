def solution(cipher, code):
    answer = ''
    #배수번째 글자만 찾아내기
    arr=[]
    arr = list(cipher)
    for i in range(0,len(cipher)):
        if((i+1)%code==0):
            answer += cipher[i]
    print(arr)
    
    return answer