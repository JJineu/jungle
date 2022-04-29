# https://www.acmicpc.net/problem/1912

from sys import stdin
input = stdin.readline

n = int(input())
nums = [0]+list(map(int, input().split()))
d = [-1e9]*(n+1)

d[1] = nums[1]
for i in range(2, n+1):
    d[i] = max(nums[i], nums[i]+d[i-1])

print(max(d))

