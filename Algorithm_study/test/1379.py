from sys import stdin 
input = stdin.readline

n = int(input())
room = []
res_room = [0]+[]
for i in range(n):
    num, start, end = map(int, input().split())
    room.append((num,start,end))
    res_room.append(num)

room.sort(key = lambda x: -x[2])
# print(*room, sep='\n')

# # end값 기준 정렬 -> 이진탐색처럼? end 첫값 끝값부터 강의실 배정
# end = room[0][2]
# for i in range(n):
#     if i == room[0]:
#         res_room[i] = 


# for i in range(1, n):
#     if i < end:


# print(res_room[1:])

