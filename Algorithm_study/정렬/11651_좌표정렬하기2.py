#좌표 정렬하기 2

# 답
# n = int(input())
 
# li = [] # 2차원리스트
# for _ in range(n):
#     xy = list(map(int,input().split()))
#     li.append([xy[1],xy[0]])
 
# li.sort()
 
# for i in li:
#     print(i[1],i[0])


n = int(input())
s= []
for _ in range(n):
    s.append(list(map(int, input().split())))

s = sorted(s, key=lambda x: (x[1], x[0]))
for i in s:
    print(*i)


#key=lambda x: (x[1], -x[0])
#x[1] 기준으로 오름차순 후, x[0] 기준으로 내림차순