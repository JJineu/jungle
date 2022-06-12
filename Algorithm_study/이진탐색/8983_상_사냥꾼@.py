# https://www.acmicpc.net/problem/8983
# 사냥꾼

from sys import stdin
input = stdin.readline


def main():
    m, n, l = map(int, input().split())
    hunt_li = list(map(int, input().split()))
    animal_li = [list(map(int, input().split())) for _ in range(n)]

    hunt_li.sort()
    # animal_li.sort()

    hunting = 0
    for x,y in animal_li:
        start = 0
        end = m-1
        while start <= end:
            mid = (start+end)//2
            area = abs(hunt_li[mid]-x) + y
            if area <= l:
                hunting += 1
                break
            else:
                if hunt_li[mid] < x:
                    start = mid + 1
                elif hunt_li[mid] > x:
                    end = mid - 1
                else:   
                    break

    print(hunting)

main()