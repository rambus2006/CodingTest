def solution(letter):
    answer = ''
    morsecode_arr = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    abc_arr = [chr(i) for i in range(ord('a'),ord('z')+1)]
    letterWithSplit = letter.split(" ")
    morseLength = len(morsecode_arr)
    for j in letterWithSplit:
        for i in range(0,len(morsecode_arr)):
            if(morsecode_arr[i] == j):
                answer+=abc_arr[i]
                break
    return answer