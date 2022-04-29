# https://www.acmicpc.net/problem/2812
# 크게만들기

from sys import stdin 
input = stdin.readline

n, k = map(int, input().split())
num = list(input())
stack = []

K = k
for i in range(n):
    while K and stack and stack[-1] < num[i]:   # 2. stack[-1]<=li[i] 이면, 88877일 때 최적의 수 888이 아니라, 877이 남는다.
        stack.pop()
        K -= 1                  # k가 while문 안에서 줄어들기 때문에, 다른 변수로 선언하여 print할때 쓰려고 함
    stack.append(num[i])        # 1. 스택에 li[0] 저장

print(''.join(stack[:n-k]))     # 9421과 같이 뒤의 두 숫자를 삭제해야 하는 경우, stack에 21이 남아있으므로
