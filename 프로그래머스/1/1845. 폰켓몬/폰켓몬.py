def solution(nums):
    kind = len(set(nums))        # 폰켓몬 종류 수
    select = len(nums) // 2      # 선택 가능한 마리 수
    
    return min(kind, select)