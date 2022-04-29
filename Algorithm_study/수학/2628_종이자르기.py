#종이자르기/수학

from itertools import product

X, Y = map(int, input().split())
N = int(input())
list_x=[]
list_y=[]

for _ in range(N):
    m, n = map(int, input().split())
    if m == 0:
        list_y.append(n)
    else:
        list_x.append(n)
list_x.append(X)
list_y.append(Y)

list_x = sorted(list_x)
list_y = sorted(list_y)

list_xxx = []
list_yyy = []

for i in range(len(list_x)):
    if i == 0:
        list_xxx.append(list_x[i])
    else:
        list_xxx.append(list_x[i]-list_x[i-1])

for i in range(len(list_y)):
    if i == 0:
        list_yyy.append(list_y[i])
    else:
        list_yyy.append(list_y[i]-list_y[i-1])

A= list(product(list_xxx, list_yyy))
mul = []
for i in range(len(A)):
    mul.append(int(A[i][0])*int(A[i][1]))
    
print(max(mul))