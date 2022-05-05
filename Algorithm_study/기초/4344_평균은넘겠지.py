#평균은 넘겠지/배열
from sys import stdin 
input = stdin.readline

c = int(input())
for i in range(c):
    score = list(map(int, input().split()))

    n = score[0]
    sum = 0
    for i in score[1:]:
        sum += i

    avg = sum / n
    cnt = 0
    for i in score[1:]:
        if i > avg:
            cnt += 1

    print(f'{round((cnt/n)*100,3):.3f}%')


