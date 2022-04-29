#사칙연산/입출력
# a = int(input()) b = int(input())

#입력받은 값을 공백을 기준으로 분리하여 변수에 차례대로 저장
# a, b = input().split()
# a = int(a)
# b = int(b)

a, b  = map(int, input().split())

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
