# 정렬된 배열에서 특정 수의 개수 구하기

# n, x = int(input().split())
# array = map(int, input().split())

# start = 0
# end = len(array)
# mid = (start+end)//2

# while start<= mid:
#     if array[mid] > x:
#         mid = end - 1  
#     elif array[mid] < x:
#         mid = start + 1
#     elif array[mid] == x:
#         start_point = mid

# while end >= mid:
#     if array[mid] > x:
#         mid = end - 1  
#     elif array[mid] < x:
#         mid = start + 1
#     elif array[mid] == x:
#         end_point = mid

# if start_point != end_point:
#     print("-1")
# else:



# 사용하기
# from bisect import bisect_left, bisect_right

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
li = list(map(int, input().split()))

right_index = bisect_right(li, x)
left_index = bisect_left(li,x)
result = right_index - left_index

if result <= 0:
    print(-1)
else:
    print(result)

