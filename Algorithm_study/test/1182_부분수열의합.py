#1182
from itertools import combinations
n,s = map(int, input().split())
count = 0

for _ in range(n):
    li = list(map(int, input().split()))

for i in range(len(li)):
    if sum(combinations(li,i)) == s:
        count += 1
print(count)


# 1182 윤우
N, S = map(int, input().split())
A = tuple(map(int, input().split()))

ans = [0]
def solve(i=0, s=0):
    if i == N:
        if s == S:
            ans[0] += 1
        return
    solve(i+1, s+A[i])
    solve(i+1, s)
solve()
print(ans[0]) if S else print(ans[0]-1) 

# li = [1,2,3,4]
# com_li = list(combinations(li,2))
# print(com_li)
# for i in range(len(com_li)):
#     print(sum(com_li[i]))




