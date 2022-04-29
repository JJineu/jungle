# 1110
N = int(input())

def cycle(n:int) -> int:
    if n < 10:
        n_s = '0' + str(n)
    else:
        n_s = str(n)
    a = n_s[-1]
    temp = str(int(n_s[0]) + int(n_s[1]))
    b = temp[-1]
    # a = n % 10
    # b = (n // 10 + n % 10) % 10
    return int(a + b)

ans = 1
new_num = cycle(N)
while new_num != N:
    new_num = cycle(new_num)
    ans += 1
print(ans)


# 1110 윤우
N = int(input())

def cycle(n):
    a = n % 10
    b = (n // 10 + n % 10) % 10
    return 10*a + b

ans = 1
new_num = cycle(N)
while new_num != N:
    new_num = cycle(new_num)
    ans += 1
print(ans)