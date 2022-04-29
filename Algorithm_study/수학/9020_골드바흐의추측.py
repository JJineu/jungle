#골드바흐의추측/수학

# case = []
# for i in range(10000):
#     flag= True
#     for j in range(2, int(i**0.5)+1):
#         if i % j == 0:
#             flag =False
#         else:
#             case.append(i)
# result =[]
# for i in range(N,0,-1):
#     for i in range(N):
#         if N / case[i] == case[j]:
#             if min(abs(int(case[i])-int(case[j]))):
#                 print(i, j)


# # 1. 테스트 케이스 개수
# N = int(input())
# s =[]
# for _ in range(N):
#     s.append(int(input()))

# # 2. 소수판별함수
# case = []
# for j in range(2,10001):
#     case.append(j)
#     for k in range(2, int(j**0.5)+1):
#         if j % k == 0:
#             continue
#         else:
#             case.append(j)
# print(case)

# # 3. 골드바흐의수가 리스트에 있는지
# # case.sort(reverse=True)
# # for k in case:
# #     if (N-k) in case:
# #         print(N-k, k)
# #         break

# for a in range(N):
#     for b in range(N//2, 0, -1):
#         if b in case and N-b in case:
#             print(N-b, b)
#             break


# 풀이
# T = int(input())

# num = [0 for i in range(10001)] #소수를 담아줄 배열
# num[0] = 1
# num[1] = 1

# for i in range(2, 10001): # 소수면 0, 아니면 1
#     if num[i] == 0: 
#         temp = i
#         k = 2
#         for j in range(2, 10001):
#             if temp * j > 10000:
#                 break
#             num[temp * j] = 1

# for i in range(T):
#     k = int(input())
#     for j in range(k // 2, k): # 반으로 나눠서 소수들의 합으로 되는지 확인
#         if num[j] == 0 and num[k - j] == 0:
#             print(f"{k - j} {j}")
#             break

#동준

import sys
input = sys.stdin.readline
m = 10000
arr = [False, False] + [True] * (m-1)
#arr=[f,f,t,t,t,t,t,,,,]

#소수 판별, 소수가 아니면 false로 바꾸기
for i in range(2,int(m**0.5)+1):
    for j in range(i+i, m+1, i):
        if arr[i]: 
            arr[j] = False
            #arr[i]=true라면 i의 배수는 전부 False

#입력된 수가 소수의 합으로 되었는지
#enumerate함수 사용
lst = []
for i in range(int(input())):
    n = int(input())
    for x,y in enumerate(arr[:n//2+1]):
        #enumerate() (인덱스, 원소) 튜플형태로 반환
        if y and arr[n-x]:
            # y가 t일때, 순서가 x: x번째 true(y)
            # arr[x] = y(true)
            # n-x번째도 true라면, 골드바흐의 수임
            lst.append([x,n-x])
    print(*lst[-1])
    #*아스테리카 사용