X=int(input())
N=int(input())
sum=0
for i in range(0,N):
    a,b=input().split()
    a=int(a)
    b=int(b)
    sum+=a*b
if X==sum:
    print("Yes")
else:
    print("No")