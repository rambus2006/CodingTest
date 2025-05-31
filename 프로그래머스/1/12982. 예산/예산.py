def solution(d, budget):
    d.sort()
    count = 0
    for money in d:
        if budget >= money:
            budget -= money
            count += 1
        else:
            break
    return count