def solution(s:str):
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    answer = 0

    for i in range(10):
        s = s.replace(number[i], str(i))
    answer = int(s)
    return answer

print(solution("one4seveneight"))
print(solution("23four5six7"))



# 숫자는 그대로 저장
# 
# 문자열 끝부분과 대칭되는지 확인 -> 그만큼 삭제해줌
#
# e, o, x 로 끝나면 -3
# o, r, e, e 로 끝나면 -4
# e, n, t 로 끝나면 -5
# e가 겹치니까 e만 따로 계산

# while s:
# 스택에 문자열 하나씩 넣기
#     for i in range(10):
#         if s[-1] == i:
#             answer.append(i)
#         else:
#             if s[-3:] == number[i]:
#                 answer.append(i)
#                 s = s[:len(s)-3]
#             elif s[-4:] == number[i]:
#                 answer.append(i)
#                 s = s[:len(s)-4]
#             elif s[-5:] == number[i]:
#                 answer.append(i)
#                 s = s[:len(s)-5]

