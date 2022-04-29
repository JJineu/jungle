# https://www.acmicpc.net/problem/2839

# 그리디

from sys import stdin
input = stdin.readline

n = int(input())

bag = 0
while n >= 0 :
    if n % 5 == 0 :  # 5의 배수이면
        bag += (n // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    n -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)


# dp

from sys import stdin
input = stdin.readline

n = int(input())

arr = [5001] * (n+5)    # N의 값이 5보다 작은 경우 Index Out of Range 오류를 잡기 위해서
arr[3] = arr[5] = 1

for i in range(6, n+1):
    arr[i] = min(arr[i-3], arr[i-5]) + 1

print(arr[n] if arr[n] < 5001 else -1)  ###