#피보나치 함수/dp

from sys import stdin 
input = stdin.readline

zero = [1,0]  # fibo(0) fibo(1) fibo(2)일때 0 호출횟수
one = [0,1]

def fibo(x):
    if x >= len(zero):
        for i in range(len(zero), x+1):
            zero.append(zero[i-1] + zero[i-2])  # fibo(i) = fibo(i-1) + fibo(i-2) 이므로 0,1 호출횟수도 동일
            one.append(one[i-1] + one[i-2])
    print(zero[x], one[x])

t = int(input())

for _ in range(t):
    fibo(int(input()))