# 못품

# n개 음이 아닌 정수
# 순서 바꾸지 않음, 더하거나 뺌
# 1-50 자연수, 2-20개, 타겟은 1-1000
# 리턴 : 경우의 수

# from itertools import product 

def solution(numbers, target):
    cnt = 0

    li = [(i, -i) for i in numbers]
    # print(li)
    def dfs(li):
        # 좌표 0, 1
        for i in range(2):


        for i in range(len(li)):
            if i == target:
                cnt +=1
        print(cnt)
    return cnt


solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)