'''
문제 분석 
구하라는 값 : 
첫번쨰 숫자가 두번쨰 숫자의 약수라면 factor를 출력, 
첫번쨰 숫자가 두번째 숫자의 배수라면 multiple을 출력 
둘 다 아니라면 neither을 출력한다. 
'''

while True: 
    num1,num2 = map(int,input().split())
    
    if num1 == 0 and num2 ==0: 
        break
    # 첫번쨰 숫자가 두번쨰 숫자의 약수라면 
    elif num2%num1 == 0:
        print('factor')
        
    elif num1%num2 == 0:
        print('multiple')
        
    else:
        print('neither')
    