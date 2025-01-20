def solution(numbers):
    answer = 0
    numarr = []
    numlen = len(numbers)
    #오름차순 정렬
    # numarr = numbers.sorted()
    numarr = sorted(numbers)
    answer = numarr[numlen-1]*numarr[numlen-2]
    return answer