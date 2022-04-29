#소수찾기/수학

#안됨
# for j in range (100):
#     for i in range(2,j):
#         if j%i != 0: listB.append(j)

# print(listB)

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


N= int(input())
s= map(int, input().split())
count = 0

for i in s:
    if i < 2:
        continue
    else:
        flag = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                flag = False
                break
        if flag:
            count += 1
print(count)


# N = int(input())
# s = map(int, input().split())
# prime = []

# for i in range(2, 1001):
#     flag = True
#     for j in range(2, int(i**0.5)+1):
#         if i%j == 0:
#             flag = False
#             break
#     if flag:
#         prime.append(i)

# count =0
# for k in s:
#     if k in prime:
#         count += 1

# print(count)
# print(prime)