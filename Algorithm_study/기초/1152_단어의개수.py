#단어의개수/문자열
#split함수 쓰면, 띄어쓰기 단위로 인덱스에 저장된다.
#리스트에 스트링을 그대로 넣으면, 문자 하나당 인덱스에 저장된다.

# s = str(input())
# count = 0
# for i in range(len(s)):
#     if (s[i]!=None & s[i+1] ==None):
#         count += 1
#         if s[int(len(s))] != " ":
#             print(count)
#         else:
#             print(count-1)

s = input().split()
print(len(s))

# s = list(map(str, input().split()))
# print(len(s))