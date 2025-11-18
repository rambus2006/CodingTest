while True:
    a,b,c = map(int,input().split())
    if a==0 and b == 0 and c  == 0:
        break
    else: 
        a_square = pow(a,2)
        b_square = pow(b,2)
        c_square = pow(c,2)
    
        if a_square + b_square == c_square:
            print('right')
        elif b_square + c_square == a_square:
            print('right')
        elif a_square + c_square == b_square:
            print('right')
        else: 
            print('wrong')