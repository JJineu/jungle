# https://www.acmicpc.net/problem/8983
# 사냥꾼

from sys import stdin 
input = stdin.readline

m, n, l = map(int, input().split())
hunt = list(map(int, input().split()))
animal = [list(map(int, input().split())) for _ in range(n)]

hunt.sort()
animal.sort()

hunting = 0

for i in animal:
    start = 0   # 인덱스로 접근
    end = m-1

    while start <= end:
        mid = (start+end)//2
        if abs(hunt[mid] - i[0]) + i[1] <= l:
            hunting += 1
            break
        else:   # 동물이 사정거리 이상이면
            if hunt[mid] > i[0]:
                end = mid -1
            elif hunt[mid] < i[0]:
                start = mid +1
            else:
                break
print(hunting)