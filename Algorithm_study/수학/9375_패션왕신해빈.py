#패션왕 신해빈

# from sys import stdin

# T = int(stdin.readline())

# for _ in range(T):
#     n = int(stdin.readline())
#     d ={}
#     for i in range(n):
#         a,b = stdin.readline().split()
#         if b not in d:
#             d[b] = [a]
#         else:
#             d[b].append(a)
#     # print(d)
    
#     # 각 키의 값의 개수 +1 * 반복
#     result = 1
#     for a in d.values():
#         result *= len(a)+1
#     print(result-1)
   

#counter함수사용 
from collections import Counter
t = int(input())

for i in range(t):
    n = int(input())
    wear = []
    for j in range(n):
        a, b = input().split()
        wear.append(b)
        
    print(wear)
    wear_Counter = Counter(wear)
    cnt = 1 # 각 종류마다 항목의 개수

    for key in wear_Counter:
        cnt *= wear_Counter[key] + 1

    print(cnt-1)




