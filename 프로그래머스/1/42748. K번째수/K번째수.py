def solution(array, commands):
    answer = []
    for idx in range(0,len(commands)):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
        # print(k)
        # print(i,j,k)
        arrlist = []
        arr=[]
        arr += array[(i-1):j]
        arr.sort(reverse=False)
        answer.append(arr[(k-1)]) 
            # print(array[num])
        #     arr.sort()
        # answer.append(arr[k])
    return answer