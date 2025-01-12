import math
def solution(n):
    answer = 0
    lcm=[];
    for i in range(max(n,6),(n*6)+1):
        if i%n==0 and i%6==0:
            lcm.append(i)
    answer = int(lcm[0]/6)
    return answer