#블랙잭/완전탐색

#완전탐색
n, m= map(int, input().split())
s = list(map(int,input().split()))

result=0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if s[i] + s[j] + s[k] > m:
                continue
            else:
                result = max(result, s[i] + s[j] + s[k])
print(result)


#조합
from itertools import combinations
N, M = map(int, input().split())
s = [""]*N
s = list(map(int, input().split()))
max_sum=0
#sum은 리스트안의 리스트를 바로 구할 수 있게 함
for c in combinations(s,3):
    if sum(c) <= M and sum(c) > max_sum:
        max_sum = sum(c)

print(max_sum)
