# from sys import stdin 
# input = stdin.readline

# s = input()
# bomb = input()
# stack = []

# for i in range(len(s)): #인덱스
#     stack.append(s[i])  #문자열
#     if stack and stack[-1] == bomb[-1] and len(stack) >= len(bomb):
#         if ''.join(stack[-len(bomb):]) == bomb:
#             for _ in range(len(bomb)):
#                 stack.pop()

# if stack:
#     print(''.join(stack)) 
# else:
#     print("FRULA")


from sys import stdin
input = stdin.readline

word = input().strip()
bomb = input().strip()

stack = []

for i in word:
    if i != bomb[-1]:
        stack.append(i)

    else:
        stack.append(i)
        b = len(bomb)
        if ''.join(stack[-b:]) == bomb:
            for _ in range(b):
                stack.pop()

if len(stack) == 0:
    print('FRULA')

else:
    print(''.join(stack))