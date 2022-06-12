# https://www.acmicpc.net/problem/2470
# 두 용액

from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.sort()

    # 이중포인터
    left = 0 
    right = n-1

    res = 10e9*2
    final = []

    while left < right:
        l = li[left]
        r = li[right]
        
        tot = l+r
        if abs(tot) < res:
            res = abs(tot)
            final = [l,r] 

        if tot < 0:
            left +=1
        else:
            right -=1

    print(*final)

main()