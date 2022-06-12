# https://www.acmicpc.net/problem/1654
# 랜선자르기

from sys import stdin 
input = stdin.readline

# n 범위 10e9, 2초 ->

def main():
    k, n = map(int, input().split())
    width = list(int(input()) for _ in range(k))

    start = 1
    end = max(width)
    res = 0

    while start <= end:             # 등호 들어가야 함 =
        mid = (start+end)//2        # 잘라낼 랜선 길이 단위
        cnt = 0
        for i in range(k):
            # if width[i]>= mid:      # 없어도 됨
            cnt += width[i]//mid

        if cnt >= n:
            res = mid
            start = mid +1
        else:
            end = mid -1

    print(res)

main()