# https://www.acmicpc.net/problem/9935

from sys import stdin 
input = stdin.readline

s = input().rstrip()        # rstrip, join 써야 답 도출됨...
bomb = input().rstrip()
stack = []

for i in range(len(s)):
    stack.append(s[i])
    
    if s[-1] == bomb[-1] and len(stack) >= len(bomb):   # 마지막 글자가 같고(앞부터하면 112ab고 12ab일때 일치하지 않음)
        
        if ''.join(stack[-len(bomb):]) == bomb:      # bomb 글자만큼 뒤로 이동한 부분부터 확인
            # del stack[-len(bomb):] 같은 의미
            for i in range(len(bomb)):
                stack.pop()

if stack:
    print(''.join(stack))
else:
    print("FRULA")
