# https://www.acmicpc.net/problem/11053
# dp

from sys import stdin 
input = stdin.readline

n = int(input())
A = list(map(int, input().split()))

# 부분수열의 길이는 변할 수 있다.
# 이진탐색으로 가능하다

A.sort()

start = A[0]
end = A[-1]
while start<=end:
    mid = (start+end)//2
    


import bisect as bs

n = int(input())
nums = [0] + list(map(int, input().split()))
dp = [0]*(n+1)
# 문제의 조건에 음수가 포함되므로 최저를 0이 아닌 -무한대로 설정해준다.
cp = [-float('inf')]

for i in range(1, n+1):
    if nums[i] > cp[-1]:
        cp.append(nums[i])
        dp[i] = len(cp)-1
    else:
        dp[i] = bs.bisect_left(cp, nums[i])
        cp[dp[i]] = nums[i]
print(len(cp)-1)

# 역추적
max_idx, ans = max(dp)+1, []
for i in range(n, 0, -1):
    if dp[i] == max_idx-1:
        ans.append(nums[i])
        max_idx = dp[i]
print(*ans[::-1])

