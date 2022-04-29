# https://www.acmicpc.net/problem/9251

from sys import stdin
input = stdin.readline

str1 = input().strip()
str2 = input().strip()

dp_matrix = [[0]*(len(str2)+1) for _ in range((len(str1)+1))]

for i in range(1, len(str1)+1):
    for j in range(1,len(str2)+1):
        if str1[i-1]==str2[j-1]:
            dp_matrix[i][j] = dp_matrix[i-1][j-1]+1
        else:
            dp_matrix[i][j] = max(dp_matrix[i-1][j],dp_matrix[i][j-1])
            
print(dp_matrix[-1][-1])

