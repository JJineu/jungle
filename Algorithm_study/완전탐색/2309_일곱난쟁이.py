#일곱난쟁이/완전탐색

#완전탐색으로 풀려면, sum-100 = 두명의 키의 합
#break 필수


# s = [0]*9
# sum_s = 0
# for _ in range(9):
#     s.append(int(input()))
#     sum_s += int(input())

# sp = list(combinations(s, 2))
# m =[]
# sum_m = 

# if sum_s-sum_m ==100:

from itertools import combinations
s = []
for _ in range(9):
    s.append(int(input()))
s.sort()
#sort를 미리하는게 좋겠다..
# s = [int(input()) for _ in range(9)]

for com_s in list(combinations(s,7)):
    if sum(com_s) == 100:        
        for i in com_s:
            print(i)
        break
    #break를 안넣어서 틀림
