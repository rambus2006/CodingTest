n1 = int(input())
n2 = int(input())

r = n2 % 10
n3 = n1 * r

r = (n2 // 10) % 10
n4 = n1 * r

r = n2 // 100
n5 = n1 * r

n6 = n3 + n4 * 10 + n5 * 100

print(n3)
print(n4)
print(n5)
print(n6)