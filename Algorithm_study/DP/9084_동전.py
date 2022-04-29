# https://www.acmicpc.net/problem/9084

from sys import stdin 
input = stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())   

    d = [0]*(m+1)
    d[0] = 1  
    
    for coin in coins:
        for i in range(m+1):
            if i >= coin:   # 인덱스가 화폐값보다 크면
                d[i] += d[i-coin]   # 인덱스-화폐값 에 대한 value(=경우의수)는 이전의 것을 더한 값

    print(d[m])

    # 인덱스가 가격, 값이 횟수
    # for i in range(n):
    #     for j in range(coin[i], m+1):
    #         if d[j-coin[i]] != 10001:
    #             d[j] = min(d[j], d[j-coin[i]]+1)
