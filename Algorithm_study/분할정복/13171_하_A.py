# https://www.acmicpc.net/problem/13171

from sys import stdin 
input = stdin.readline

A = int(input())
X = int(input())

def multi(a, x):
    if x == 1:
        return a % 1000000007

    temp = multi(a, x//2)
    if x%2 == 1:
        return (temp*temp*a)%1000000007
    else:
        return (temp*temp)%1000000007

print(multi(A,X))

    