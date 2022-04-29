#문자열반복/문자열
t = int(input())

for _ in range(t):
    r, s = input().split()
    for i in range(len(s)): #s를 자동으로 리스트화 시키는지
        p = s[i]*int(r)
        print(p, end='')
    print()

# T = int(input())
# for i in range(T):
#     a, s = input().split()
#     for j in s:
#         print(int(a)*j, end="")
#     print()