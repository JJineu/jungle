def solution(orders, course):
    orders = orders
    course = course
    answer = []

    d = [0] * 91
    for i in range(len(orders)):
        for j in orders[i]:
            # print(orders[i])
            d[ord(j)] += 1
            # print(d[90])

    for i in course:
        com = []
        for j in range(65, 91):
            if d[j] >= 2:   # 잘못생각함. 두명의 주문에, 결과에 나오는 코스메뉴가 들어가 있어야 함.
                com.append(str(j))

    # print(com)
    return answer

# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
# print(ord('Z')) # 65-90


# 정답코드

from collections import Counter
from itertools import combinations

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            # order.sort()
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        # most_common 데이터의 개수가 많은 순으로 정렬된 배열을 리턴
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]
        # [('AC', 3), ('BD', 2), ('BC', 1) ]
        # result += ['AC', 'BD']
        
    return [ ''.join(v) for v in sorted(result) ]