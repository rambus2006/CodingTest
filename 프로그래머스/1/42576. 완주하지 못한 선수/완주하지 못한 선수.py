# 1. 이름별 개수를 세는 함수

def count_hash(array):
    count = {}

    for name in array:
        if name in count:
            count[name] += 1
        else:
            count[name] = 1

    return count


# 2. 각각 개수 세기
def solution(participant, completion):
    answer = ''

    participant_dict = count_hash(participant)
    completion_dict = count_hash(completion)


    # 3. 완주자 개수 빼기

    for name in completion_dict:
        participant_dict[name] -= completion_dict[name]


    # 4. 남은 사람 찾기

    for name in participant_dict:
        if participant_dict[name] > 0:
            answer = name

    return answer