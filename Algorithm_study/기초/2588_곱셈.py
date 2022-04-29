#곱셈/입출력
a = input()
b = input()
a = int(a)

print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*int(b[2])+10*a*int(b[1])+100*a*int(b[0]))

#모듈 안됨
from sys import stdin
a, b = map(int, stdin.readline().strip())

print(a*(b%10))
print(a*(b%100-b%10))
print(a*(b//100))
print(a*b)