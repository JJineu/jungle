# https://www.acmicpc.net/problem/2493
# 탑

from sys import stdin 
input = stdin.readline

n = int(input())
top_li = list(map(int, input().split()))

stack = []      # 레이저를 수신할 탑의 위치를 저장(현재 탑보다 height가 큰 것)
receive = [0]*n # 레이저를 수신받은 탑의 위치(현재 탑보다 근접한 높은탑)

for i in range(n):
    while stack and top_li[stack[-1]] < top_li[i]:  # 스택이 존재하고, 현재 탑크기보다 마지막 스택이 작으면
        stack.pop()                                 # 마지막 저장값을 날리고(계속 반복)

    if stack:                       # while문을 마치고도 스택이 있으면 = i보다 큰탑
        receive[i] = stack[-1] + 1  # i위치에 수신받은 위치값 저장(0부터 시작한 index이므로 +1)
    
    stack.append(i)

print(*receive)
