# https://www.acmicpc.net/problem/2805
# 나무자르기

# 백준 통과 // syntax error near unexpected token `('

n, m = map(int, input().split())
tree_li = list(map(int, input().split()))

start = 0
end = max(tree_li)
result = 0

while start <= end:
    mid = (start+end)//2
    sum = 0
    for i in tree_li:
        if i > mid:
            sum += i - mid
    
    if sum < m:
        end = mid -1
    else:
        result = mid
        start = mid + 1

print(result)