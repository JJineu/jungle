# https://www.acmicpc.net/problem/15815

# from sys import stdin 
# input = stdin.readline

s = input()
stack = []

for i in range(len(s)):
    try:
        stack.append(int(s[i]))
    except:
        if s[i] == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        elif s[i] == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)        
        elif s[i] == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)  
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)

print(*stack)    