#달팽이는 올라가고 싶다/문자열
from sys import stdin
import math 

a,b,v = map(int, stdin.readline().split())

print(math.ceil((v-b)/(a-b)))
# ceil 올림
# floor 내림 != int 소숫점아래 버림
# 소수점 조절하려면 먼저 곱하고, 올림 내림 사용할 것
# round 반올림


# 시간초과
# for i in range(1, 100000000):
#     if v== a*i-b*(i-1):
#         print(i)
#         break