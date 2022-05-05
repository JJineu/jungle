#소수찾기/수학

#isPrime함수
# n=100
# def isPrime(a):
#     if(a<2):
#         return False
#     for i in range(2,a):
#         if(a%i==0):
#             return False
#     return True
# for i in range(n+1):
#     if(isPrime(i)):
#         print(i)
        
# n = int(input())
# listA = map(int, input().split())
# count = 0
# error =0


# for j in listA:
#     for i in range(2, j):
#         if n%i == 0:
#             error += 1
#         if error == 0:
#             count += 1
# print(count)


from sys import stdin 
input = stdin.readline

n = int(input())

prime = []
for i in range(2,1001):
    flag = True
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            flag = False
            break
    if flag:
        prime.append(i)

test_n = list(map(int, input().split()))
count = 0
for test in test_n:
    if test in prime:
        count += 1
print(count)


# 에라토스테네스의 채
n = int(input())

prime = [False, False] + [True] * (999)  # true이면 소수
for i in range(2, int(1001 ** 0.5) + 1):
    if prime[i]:
        for j in range(2*i, 1001, i):
            prime[j] = False

test_n = list(map(int, input().split()))
count = 0
for test in test_n:
    if prime[test]:
        count += 1
print(count)