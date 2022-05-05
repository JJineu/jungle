from sys import stdin
input = stdin.readline

# n = int(input())
# graph = [list(map(int, input().split())) for _ in range(n)]
# visit = [[0]*n for _ in range(n)]

# res = []
# sum_li = 0
# def dfs(depth):
#     global sum_li
#     if depth == n:
#         sum_li = max(sum_li, sum(res))
#         return 

#     for i in range(n):
#         for j in range(n):
#             if visit[i][j]:
#                 continue
#             visit[i][j] = 1
#             res.append(graph[i][j])
#             dfs(depth+1)
#             visit[i][j] = 0
#             res.pop()
# dfs(0)
# print(print(sum_li))


n = int(input())
nums = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())

min_nums = 1e9
max_nums = -1e9

def cal(depth, total, plus, minus, multiply, divide):
    global min_nums
    global max_nums


    if depth == n:
        max_nums = max(max_nums, total)
        min_nums = min(min_nums, total)
        # print(max_nums)
        return       

    if plus:
        cal(depth+1, total+nums[depth], plus-1, minus, multiply, divide)
        print(nums[depth])
    if minus:
        cal(depth+1, total-nums[depth], plus, minus-1, multiply, divide)
    if minus:
        cal(depth+1, total*nums[depth], plus, minus, multiply-1, divide)
    if minus:
        cal(depth+1, int(total/nums[depth]), plus, minus, multiply, divide-1)

cal(1,nums[0],plus,minus,multiply,divide)
print(max_nums)
print(min_nums)