xlist = []
ylist = []
result = []

def finddot(li):
    # 우리 처음으로 돌아가자. 배열인덱스로 하던
    for i in range(len(li)):
        if li.count(li[i]) == 1:
            result.append(li[i])


for i in range(0,3):
    x,y = map(int,input().split())
    xlist.append(x)
    ylist.append(y)
    
finddot(xlist)
finddot(ylist)

print(" ".join(map(str,result)))



