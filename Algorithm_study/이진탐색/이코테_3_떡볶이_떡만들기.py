# 떡볶이 떡 만들기

n, m = map(int, input().split())
ddeock_li = list(map(int, input().split()))

start = 0
end = max(ddeock_li)
result = 0


while start <= end:
    re_sum = 0
    mid = (start+end)//2
    for i in ddeock_li:
        if i > mid:
            re_sum += i-mid

    if re_sum < m:
        end = mid-1
    else:
        result = mid
        start = mid +1

print(result)