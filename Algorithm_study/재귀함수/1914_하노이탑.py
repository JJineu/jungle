#하노이탑/재귀함수
# hanoi(n, from, to, other)
# def hanoi(n,a,b,c):
#     if n == 1:
#         print(a,c)
#     else:
#         hanoi(n-1,a,c,b)
#         print(a,c)
#         hanoi(n-1,b,a,c)
# cur = 0
# i = 0

# N = int(input())
# while i < N:
#     cur = 2*cur +1
#     i +=1
# print(cur)
# if N <= 20:
#     hanoi(N,1,2,3)

def hanoi(n,a,b):
    if n==1:
        print(a,b)
        return
    if n > 1:
        hanoi(n-1,a,6-a-b)
        print(a,b)
    if n > 1:
        hanoi(n-1,6-a-b,b)

n= int(input())
print(2**n-1)
if n<=20:
    hanoi(n,1,3)


#정답
def hanoi(n, start, m, goal):
#n개의 원판이 start에 있을때, other기둥으로 모두 이동시키는 함수
    if n == 1:
        print(start, goal, sep = " ")
    else:
        hanoi(n-1, start, goal, m)
        hanoi(1, start, m, goal)
        hanoi(n-1, m, start, goal)

n = int(input())
print(2**n-1)
if n<=20:
    hanoi(n,1,2,3)