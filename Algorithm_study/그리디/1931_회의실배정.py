# https://www.acmicpc.net/problem/1931

n = int(input())
con = [list(map(int,input().split())) for _ in range(n)]

con = sorted(con, key = lambda x:(x[1], x[0]))
# print(con)
start, end = con[0]
count=1
for i in range(1,len(con)):
    s, e = con[i]
    if s >= end:
        start = s
        end = e
        count += 1
print(count)
