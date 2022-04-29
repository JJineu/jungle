# https://www.acmicpc.net/problem/1920
# 수찾기

from sys import stdin
input = stdin.readline
n = int(input())
array = list(map(int, input().split()))
m = int(input())
target_list = list(map(int, input().split()))

array.sort()

# 인덱스로 접근

for target in target_list:
    start = 0
    end = n-1
    result = False

    while start <= end:
        mid = (start + end)//2
        if target == array[mid]: 
            result = True
            print(1)
            break

        elif target > array[mid]:
            start = mid +1
        else:
            end = mid -1

    if not result:
        print(0)