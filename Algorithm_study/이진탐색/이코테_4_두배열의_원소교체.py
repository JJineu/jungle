# 두 배열의 원소 교체

n, k = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

cycle = 1e9

li_a.sort()
li_b.sort(reverse=True)

for i in range(k):
    if li_a[i] < li_b[i]:
        li_a[i], li_b[i] = li_b[i], li_a[i]

print(sum(li_a))



