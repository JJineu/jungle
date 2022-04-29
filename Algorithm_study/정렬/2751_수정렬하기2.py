#수정렬하기2/정렬
import sys

N=int(sys.stdin.readline())
s = [int(sys.stdin.readline().strip()) for i in range(N)]

s.sort()
for i in s:
    print(i)

