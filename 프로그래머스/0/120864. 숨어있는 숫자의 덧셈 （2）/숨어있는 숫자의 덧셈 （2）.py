import re
def solution(my_string):
    return sum(map(int, ''.join(c if c.isdigit() else ' ' for c in my_string).split()))

    