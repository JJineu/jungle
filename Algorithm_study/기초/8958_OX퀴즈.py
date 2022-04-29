from sys import stdin 
input = stdin.readline

t = int(input())
for _ in range(t):
    s = input()
    sum = 0
    tmp = 0
    for i in s:
        if i == 'O':
            tmp += 1
            sum += tmp
        else:
            tmp = 0
    print(sum)