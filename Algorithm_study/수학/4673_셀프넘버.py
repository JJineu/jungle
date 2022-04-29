#셀프넘버/브루트포스 알고리즘

# all = [0]*10000
# for i in range(1,10001):
#     all.append(i)

# def non_self_number(n,):
#     for j in range(10001):

#         return n+1, non_self_number()

natural_num = set(range(1,10001))
generate_num = set()
for i in range(1,10001):
    for j in str(i):
        i += int(j)
    generate_num.add(i)

self_num = sorted(natural_num - generate_num)

for i in self_num:
    print(i)
