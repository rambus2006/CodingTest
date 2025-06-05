N = int(input())
data = []
for _ in range(N):
    age,name = input().split()
    data.append([int(age),name])
    
for i in sorted(data,key=lambda  x: x[0]):
    print(i[0],i[1])