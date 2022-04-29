# https://www.acmicpc.net/problem/1629
# 곱셈 # a^b %c

a,b,c = map(int, input().split())

# (A*B)%C == (A%C)*(B%C)%C

# 틀림
# while b > 1:
#     if a>c:
#         a = a%c

#     elif a<c:
#         a = (a*a)%c
#         b = b//2
#         if b//2 != 0:
#             b += 1
#     else:
#         print(0)

# print(a%c)

# 반례 print(4 ** 3 % 5)


# 정답
import sys
a,b,c = map(int,sys.stdin.readline().split())

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c
          
print(multi(a,b))