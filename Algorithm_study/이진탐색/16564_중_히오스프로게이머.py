# https://www.acmicpc.net/problem/16564
# 히오스 프로게이머

# 떡 자르기의 반대

from sys import stdin
input = stdin.readline

# 파라메트릭 서치
def main():
    n, k = map(int, input().split())
    level_li = list(int(input()) for _ in range(n))
    level_li.sort()
    
    start = min(level_li)
    end = start + k
    t = 0
    while start <= end:
        mid = (start+end)//2
        tmp = 0
        for level in level_li:
            if level < mid:
                tmp += mid - level

        if tmp > k:
            end = mid -1
        else:
            start = mid +1
            t = mid 

    print(t)

main()