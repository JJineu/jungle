#일곱난쟁이/완전탐색

# 

# from sys import stdin
# input = stdin.readline

# height = list(int(input()) for _ in range(9))
# height.sort()
# sum_h = sum(height)

# for i in range(8):
#     for j in range(i+1, 9):
#         if sum_h - height[i] - height[j] == 100:
#             x, y = height[i], height[j]

# height.remove(x)
# height.remove(y)

# for i in height:
#     print(i)



# # combinations

# from sys import stdin
# from itertools import combinations
# input = stdin.readline

# height = list(int(input()) for _ in range(9))
# height.sort()

# for h in list(combinations(height,7)):
#     if sum(h) == 100:        
#         for i in h:
#             print(i)
#         break   # 반복문 탈출



# recursive


# dfs

from sys import stdin
input = stdin.readline

height = list(int(input()) for _ in range(9))

result = []
visit = [0]*9

def dfs(depth, start):
    if depth == 7:
        if sum(result) == 100:
            result.sort()
            for r in result:
                print(r)
            exit(0)

    for i in range(start, 9):
        if visit[i] == 0:
            result.append(height[i])
            visit[i] = 1
            dfs(depth + 1, i)

            result.pop()  
            visit[i] = 0

dfs(0, 0)


