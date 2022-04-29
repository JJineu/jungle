#수정렬하기3/정렬

# 도수정렬 
# 메모리초과

from sys import stdin

s = [0]*10001
N = int(stdin.readline())

for _ in range(N):
	s[int(stdin.readline())] += 1

for i in range(10001):
	if s[i]:
		for _ in range(s[i]):
			print(i)
