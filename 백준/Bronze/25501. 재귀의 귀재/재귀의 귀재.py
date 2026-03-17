def recursion(s, l, r,count):
    count+=1
    if l >= r: return (f"{1} {count}")
    elif s[l] != s[r]: return (f"{0} {count}")
    else: return recursion(s, l+1, r-1,count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1,0)



T = int(input())
for tc in range(1,T+1):
    s = input()
    count = 0
    print(isPalindrome(s))
