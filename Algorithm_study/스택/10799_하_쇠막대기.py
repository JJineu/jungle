# https://www.acmicpc.net/problem/10799
# 쇠막대기

from sys import stdin 
input = stdin.readline

l = input()
stack = []
count = 0

# for문 돌릴때 i가 인덱스인지 원소인지 쓰고 시작할것
for i in range(len(l)):
    if l[i] == '(':                # 쇠막대기 개수
        stack.append(l[i])
    else:
        if len(stack) == 0:      # i == ")"일때 
            break                     
        elif l[i-1] == '(':    # 닫힌괄호 == 레이저
            stack.pop()
            count += len(stack) # 잘린 쇠막대기 추가            
        else:
            stack.pop()         # 쇠막대기 끝남
            count += 1

print(count)