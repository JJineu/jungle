#차이를최대로/완전탐색

#순열
from itertools import permutations
from sys import stdin
N = int(stdin.readline())
s = list(map(int, stdin.readline().split()))

result = 0
for com in permutations(s):
    sum = 0 #+=쓰기전에 선언할 것, for문 돌때 초기화
    for i in range(N-1):
        sum += abs(com[i]-com[i+1])
    result = max(result,sum)
print(result)


# 백트래킹
from sys import stdin
N = int(stdin.readline())
num = list(map(int, stdin.readline().split()))

li = []
result = []
check = [0]*N

def abs_sum(depth):
    if depth == N:
        result.append(sum(abs(li[i+1]-li[i])for i in range(N-1)))
        return
    for i in range(N):
        if check[i]:
            continue
        li.append(num[i])
        check[i]=1

        abs_sum(depth+1)

        li.pop()
        check[i]=0

abs_sum(0)
print(max(result))