def solution(my_string):
    answer = ''
    li = list(my_string)
    lilen = len(li)
    for i in range(0,lilen):
        if not (li[i] == 'a' or li[i] =='e' or li[i]=='i' or li[i]=='o' or li[i]=='u'):
            answer += li[i]
    return answer