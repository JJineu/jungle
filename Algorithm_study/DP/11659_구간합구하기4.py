# https://www.acmicpc.net/problem/11659

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
d = [0]*(n+1)

# prefix_sum 구간합계산 알고리즘
sum = 0
prefix_sum = [0]
for i in nums:
    sum += i
    prefix_sum.append(sum)

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j]-prefix_sum[i-1])

# d[i] : a[1]+a[2]+ ... +a[i]
# d[i] = d[i-1] + nums[i]
# a[i]+a[i+1]+a[i+2]+ ... +a[j] = d[j] - d[i-1]

