# # https://www.acmicpc.net/problem/12789

# from sys import stdin 
# from collections import deque
# input = stdin.readline

# n = int(input())
# li = deque([map(int, input().split())])
# stack = []

# i = 1
# while li:   # 리스트가 없을 때까지 반복 
#     if li and li[0] == i:
#         li.popleft()
#         i+=1
#     else:
#         stack.append(li.popleft())

#     while stack and stack[-1] == i:     # 스택의 맨 마지막 값이 i가 아닐 때까지 pop
#         stack.pop()
#         i+=1

# if stack:
#     print("Sad")
# else:
#     print("Nice")


input = __import__('sys').stdin.readline
from collections import deque
n = int(input())
q = deque(map(int, input().split()))
stack = deque()
i = 1
while q:
    if q and q[0] == i:
        q.popleft()
        i += 1
    else:
        stack.append(q.popleft())
    while stack and stack[-1] == i:
        stack.pop()
        i+=1
print('Nice' if not stack else 'Sad')