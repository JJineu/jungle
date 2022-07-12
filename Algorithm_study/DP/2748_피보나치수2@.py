# https://www.acmicpc.net/problem/2748

# top-down
from sys import stdin 
input = stdin.readline

d = [0]*91  # dp테이블 초기화

def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1

    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(int(input())))


# bottom-up
from sys import stdin 
input = stdin.readline

d = [0]*91  

d[0] = 0
d[1] = 1
n = int(input())

for i in range(2,n+1):
    d[i] = d[i-1]+d[i-2]

print(d[n])


input = __import__('sys').stdin.readline
def main():
    n = int(input())
    dp = [0,1] + [0]*(n-1)
    for i in range(n+1):
        if i == 0 or i == 1:
            continue
        else:
            dp[i] = dp[i-1]+ dp[i-2]
    
    print(dp[n])
main()