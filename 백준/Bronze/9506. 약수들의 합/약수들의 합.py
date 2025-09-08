while True: 
    num = int(input())
    
    if num == -1:
        break
    li = []
    for i in range(1,num):
        if num % i ==0:
            li.append(i)
    
    if sum(li) == num:
        li.sort()
        strlist = list(map(str,li))
        res = " + ".join(strlist)
        print(f"{num} = {res}")
    else: 
        print(f"{num} is NOT perfect.")