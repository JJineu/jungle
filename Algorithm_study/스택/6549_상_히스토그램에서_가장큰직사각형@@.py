# https://www.acmicpc.net/problem/6549
# 히스토그램에서 가장 큰 직사각형

# from sys import stdin 
# input = stdin.readline

# while int(input()) != 0:
#     n, height = int(input()), list(map(int, input().split()))
#     stack = []
#     stack.append(max)

#     for i in range(n):  # height 리스트의 0~n-1까지 탐색
#         count = 1
#         while height[i] <= count:   # 높이가 0이면 pass
#             for j in range(i, n):   # height[i]를 기준으로 그 다음 index부터 탐색
#                 if height[j] >= count:
#                     count += 1
#                 else:
#                     break
#             stack.append(count*


# for i in range(n):
#     while stack and tower[stack[-1]] < tower[i]: # 스택이 존재하고, 현재 탑크기보다 마지막 스택이 작으면
#         stack.pop()                              # 마지막 저장값을 날리고(계속 반복)
#     if stack:                           # while문을 마치고도 스택이 있으면
#         receive[i] = stack[-1] + 1      # 수신한 타워 위치(저장할때 현재위치-1이므로 +1을 해준다) 저장
#     stack.append(i)     # 스택에 i == 현재 위치-1 저장

# 민우

from sys import stdin
input = stdin.readline
while True:
    N, *rect = list(map(int, input().split())) + [0]
    if N == 0:
        break
    stack = []
    max_area = 0

    for W, H in enumerate(rect):
        while stack and H < stack[-1][1]:
            pre_width, pre_height = stack.pop()
            width = (W - stack[-1][0] - 1 if stack else W)
            max_area = max(max_area, width * pre_height)
        stack.append([W, H])
    print(max_area)