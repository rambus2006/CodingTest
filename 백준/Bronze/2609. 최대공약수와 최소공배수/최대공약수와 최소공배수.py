'''
문제 풀이 

'''
num1,num2 = map(int,input().split())

# 최대공약수 
def gcd(num1,num2):
    while num2 !=0: 
       tmp = num2
       num2 = num1 % num2
       num1 = tmp
    return num1

# 최소공배수
def lcm(num1,num2):
    # num1이 num2로 안나누어지면 됨. 거꾸로도 동일. 
    res = (num1*num2)//gcd(num1,num2)
    return res

print(gcd(num1,num2))
print(lcm(num1,num2))