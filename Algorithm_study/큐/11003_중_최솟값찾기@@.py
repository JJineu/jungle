# https://www.acmicpc.net/problem/11003
# 최솟값 찾기
# 모노톤 스택 이용

from sys import stdin 
input = stdin.readline
from collections import deque

n, l = map(int, input().split())
A = list(map(int, input().split()))
q = deque()
D = [0]*n

for i in range(n):
    while q and q[-1][1] > A[i]:
        q.pop()
    if q and i - q[0][0] >= l:  # 인덱스의 차
        q.popleft()

    q.append([i, A[i]])
    D[i] = q[0][1]      # d의 i위치에 q[0][1] =~= A[i] 입력

print(*D)

# for문 쓸것 - 인덱스로 시작
# while문은 현재 인덱스가 최솟값인지 구하려고 쓸 것
# l이 주어졌으므로, 일정시점이 지난 q안의 원소를 제거할 것 -> 저장할때 위치와 원소를 같이 저장


# from collections import deque

# n, l = map(int, input().split()) 
# arr = [*map(int, input().split())] 
# m = deque() 

# for i in range(n): 
#     tmp = arr[i] 

#     while m and m[-1] > tmp: 
#         m.pop() 
#     m.append(tmp) 
        
#     #윈도우 크기보다 커진 단계에서 arr와 비교한 후 left pop 
#     if i >= l and m[0] == arr[i - l]: 
#         m.popleft() 
#     print(m[0], end=' ')
