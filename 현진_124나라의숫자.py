# 1 -> 1
# 2 -> 2
# 3 -> 4
# 4 -> 11
# 3으로 나눠서 자리수를 바꿔주고 대입

# 1자리수 -> 3 == 3^1 
# 2자리수 -> 9 == 3^2 
# 3자리수 -> 3^3

def solution(n):
    answer = ''
    
    length = n // 3 
    d = [0]*(n+1)
    def cycle(n):
        # n = n-1 + n-2 + ...
        # n = 3*3*a + 3*2*a + 3*1*a + a
    n % 3 == 1 # 1
    n % 3 == 2 # 2
    n % 3 == 0 # 4
    
    return answer

solution(1)
solution(2)
solution(3)