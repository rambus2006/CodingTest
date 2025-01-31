import re
def solution(polynomial):
    answer = ''
    sum = 0
    num=0
    arr = list(polynomial.split(" "))
    for i in range(0,len(arr)):
        #x계산 
        if arr[i].find('x') != -1:
            # x가 1인 경우 
            if arr[i]=='x':
                sum+=1
            #x가 1이 아닌 경우 
            else:
                sum += int(arr[i].replace('x',' '))
                
        #숫자 계산 
        elif arr[i] != "+":
            num+=int(arr[i])
    
    #출력 
    #뒤의 숫자가 0 인 경우 생략해서 출력
    if num==0 and sum==1:
        answer=f"x"
    elif num==0:
        answer = f"{sum}x"
    #x 값이 0인 경우 숫자만 출력
    elif sum==0:
        answer = f"{num}"
    # x 앞의 결과가 1인 경우 생략
    elif sum ==1:
        answer = f"x + {num}"
    #모두다 아닌 경우
    else:
        answer = f"{sum}x + {num}"
        
    return answer