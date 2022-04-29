from sys import stdin 
input = stdin.readline
from itertools import permutations

n = int(input())
k = int(input())
cards = list(int(input()) for _ in range(n))

K = k
res = []
while K:
    for i in range(n):
        res.append(cards[i])

    K -= 1


print(len(set(res)))


check = [0]*n
# 조합 카드
temp = []
# 중복없는 카드
result = set()

def card(N):
    if N == k:
        result.add(''.join(temp))
        return

    for i in range(n):
        if check[i]: continue
        check[i] = 1
        temp.append(arr[i])

        card(N+1)

        check[i] = 0
        temp.pop()
        
card(0)
print(len(result))