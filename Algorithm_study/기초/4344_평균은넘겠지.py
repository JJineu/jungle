#평균은 넘겠지/배열
n = int(input())

for _ in range(n):
    list_a = list(map(int, input().split()))
    avg = sum(list_a[1:])/list_a[0]
    count = 0
    for i in list_a[1:]:
        if i>avg:
            count += 1
    avg_per = count/list_a[0]*100
    print(f"{round(avg_per,3):.3f}%")



