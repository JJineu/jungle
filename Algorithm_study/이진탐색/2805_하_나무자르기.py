# https://www.acmicpc.net/problem/2805
# 나무자르기

# 파이썬 시간초과, pypy 통과

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))


start = 0
end = max(trees)
res = 0
while start <= end:
    mid = (start+end)//2
    sum_t = 0
    for tree in trees:
        if tree > mid:
            sum_t += tree-mid

    if sum_t < m:
        end = mid-1
    else:
        start = mid+1
        res = mid

print(res)