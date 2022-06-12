# https://www.acmicpc.net/problem/2504
# 괄호의 값

from sys import stdin
input = stdin.readline

def main():
    s = input().rstrip()    # rstrip 필수

    tmp = 1
    sum = 0
    stack = []
    # 문제 1: 괄호 양쪽이 매칭이 안됨 -> stack pop
    # 문제 2: 닫는 괄호가 먼저 나옴 -> not stack: break
    # 문제 3: [), (] 상황 -> stack[-1] 확인
    for i in range(len(s)):
        if s[i] == '(':
            tmp *= 2
            stack.append(s[i])
        elif s[i] == '[':
            tmp *= 3
            stack.append(s[i])
        #  괄호를 닫을 때는 누적된 값을 결과에 저장하고, 괄호를 stack에서 빼면서 누적된 계산값도 원래대로 돌려준다.
        elif s[i] == ')':
            if not stack or stack[-1] == '[':
                sum = 0
                break
            # 직전에 맞는 괄호가 나왔을 때 계산값을 저장한다. 
            # 예를 들어 [()]의 경우 앞에서(')') 계산을 끝냈으므로, 뒤에서는(']') 값 갱신없이 넘어간다.
            if s[i-1] == '(':
                sum += tmp
            tmp //= 2           # /= 로 계산하면 sum이 float형으로 바뀜
            stack.pop()
        else:   # ']'
            if not stack or stack[-1] == '(':
                sum = 0
                break
            if s[i-1] == '[':  
                sum += tmp
            tmp //= 3
            stack.pop()
    
    if stack:
        sum = 0
    
    print(sum)

main()