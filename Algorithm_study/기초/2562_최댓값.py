#최댓값/배열
a = []
for i in range(9):
    a.append(int(input()))

print(max(a), a.index(max(a))+1)

# a=[*map(int,open(0))]

# print(*max((int(input()), i+1)for i in range(9)))